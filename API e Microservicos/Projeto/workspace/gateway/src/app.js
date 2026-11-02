import express from 'express';
import axios from 'axios';
import {createProxyMiddleware} from 'http-proxy-middleware';

const app = express();

app.use(express.json());

const serviceInstances = {};
const roudRobinIndex = {};

const getServiceUrls = async (serviceName) => {
    try{
        const response = await axios.get(`${process.env.SERVICE_REGISTRY_URL}/services/${serviceName}`);
        console.log(response.data.urls);
        return response.data.urls;
    }catch(error){
        console.error(`Error fetching service URLs: ${serviceName}: ${error.message}`);
        return [];
    }
}

const getNextServiceUrl = (serviceName) => {
    if(!serviceInstances[serviceName] || serviceInstances[serviceName].length === 0){
        return null;
    }
    const urls = serviceInstances[serviceName];
    roudRobinIndex[serviceName] = (roudRobinIndex[serviceName] + 1) % urls.length;
    return urls[roudRobinIndex[serviceName]];
}

app.use('/:serviceName/*', async (req, res, next)=>{
    const {serviceName} = req.params;
    
    if(!serviceInstances[serviceName] || serviceInstances[serviceName].length === 0){
        const urls = await getServiceUrls(serviceName);
        if(urls.length > 0){
            serviceInstances[serviceName] = urls;
            roudRobinIndex[serviceName] = 0;
        }else{
            return res.status(404).json({message: `Service not found ${serviceName}`});
        }
    }
    
    const serviceUrl = getNextServiceUrl(serviceName);
    console.log(`Proxying to: ${serviceUrl}`);
    if(serviceUrl){
        const endpoint = req.originalUrl.replace(`/${serviceName}/`, '');
        createProxyMiddleware({
            target: `${serviceUrl}/${endpoint}`,
            on: {
            proxyReq: (proxyReq, req, res) => {
                if(req.body){
                    const bodyData = JSON.stringify(req.body);
                    proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
                    proxyReq.write(bodyData);
                }
            }
            }
        })(req, res, next);
    }else{
        return res.status(404).json({message: `Service not found ${serviceName}`});
    }
});
    

app.listen(process.env.PORT, ()=>{
    console.log(`App running on port: ${process.env.PORT}`)
});
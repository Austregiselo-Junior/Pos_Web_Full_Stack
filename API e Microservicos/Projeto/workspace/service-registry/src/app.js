import express from 'express';

const app = express();

app.use(express.json());

const service = {};

app.post("/register", (req, res)=>{
    const {name, url} = req.body;

    if(!service[name]){
        service[name] = [];
    }

    const index = service[name].indexOf(url);
    
    if(index === -1){
        service[name].push(url);
        console.log(`Service registered: ${name} at ${url}`);
        res.status(200).json({message: `Service registered: ${name} at ${url}`});
        return
    }

    console.log(`Service already registered: ${name}`);
    res.status(200).json({message: `Service already registered: ${name}`});
});

app.get("/services/:name", (req, res)=>{
    const {name} = req.params;

    const urls = service[name];

    if(urls && urls.length > 0){
        res.status(200).json({urls});
    }else{
        res.status(404).json({message: "Service not found."});
    }
});

app.get("/", (req, res)=>{
    res.json({service});
});

app.listen(process.env.PORT, ()=>{
    console.log(`App running on port ${process.env.PORT}`);
});
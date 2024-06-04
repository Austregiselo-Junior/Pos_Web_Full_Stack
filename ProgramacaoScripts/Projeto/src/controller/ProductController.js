import ProductService from "../service/ProductService.js";

    export default class ProductController{
        // Define o método estático assíncrono 'create' com os parâmetros 'req' e 'res'
        static async create(req, res) {
            try {
                // Extrai 'name', 'description', 'state' e 'purchased_at' do corpo da requisição (req.body)
                const { name, description, state, purchased_at } = req.body;

                // Chama o método 'create' do 'ProductService' passando os parâmetros necessários e aguarda a criação do produto
                const product = await ProductService.create(req, name, description, state, purchased_at);

                // Retorna uma resposta HTTP 201 (Created) com o produto criado em formato JSON
                res.status(201).json({ product });
            } catch (error) {
                // Se ocorrer um erro, define o status code do erro como o status code do erro lançado ou 500 (Internal Server Error) se não estiver definido
                error.statusCode = error.statusCode || 500;

                // Retorna uma resposta HTTP com o status code do erro e a mensagem de erro em formato JSON
                res.status(error.statusCode).json({ error: error.message });
            }   
        }


        // Define o método estático assíncrono 'index' com os parâmetros 'req' e 'res'
        static async index(req, res) {
            try {
                // Extrai 'page' e 'limit' dos parâmetros da query string da requisição (req.query)
                // Define valores padrão para 'page' como 1 e 'limit' como 10, caso não sejam fornecidos
                const { page = 1, limit = 10 } = req.query;

                // Chama o método 'index' do 'ProductService' passando 'page' e 'limit' e aguarda a obtenção dos produtos
                const products = await ProductService.index(page, limit);

                // Retorna uma resposta HTTP 200 (OK) com a lista de produtos em formato JSON
                res.status(200).json({ products });
            } catch (error) {
                // Se ocorrer um erro, define o status code do erro como o status code do erro lançado ou 500 (Internal Server Error) se não estiver definido
                error.statusCode = error.statusCode || 500;

                // Retorna uma resposta HTTP com o status code do erro e a mensagem de erro em formato JSON
                res.status(error.statusCode).json({ error: error.message });
            }
        }

        static async show(req, res){
            try{
                res.json({message:"show"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async update(req, res){
            try{
                res.json({message:"update"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async delete(req, res){
            try{
                res.json({message:"delete"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async showUserProducts(req, res){
            try{
                res.json({message:"showUserProducts"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async showRecieverProducts(req, res){
            try{
                res.json({message:"showRecieverProducts"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async schedule(req, res){
            try{
                res.json({message:"schedule"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }

        static async concludeDonation(req, res){
            try{
                res.json({message:"concludeDonation"});
            }catch(error){
                error.statusCode = error.statusCode || 500;
                res.status(error.statusCode).json({error: error.message});
            }
        }
    }
import { Router } from "express";
import ProductController from "../controller/ProductController.js";
import { verifyJwt } from "../helpers/manager-jwt.js";
import imageUpload from "../helpers/image-upload.js";

// Importa o objeto Router do framework de rotas para criar um novo roteador.
const router = Router();

// Define uma rota POST na raiz ("/") que usa middlewares verifyJwt e imageUpload para verificação de JWT e upload de imagens, respectivamente, e chama o método create do ProductController.
router.post("/", verifyJwt, imageUpload.array("images"), ProductController.create);

// Define uma rota GET na raiz ("/") que chama o método index do ProductController para listar todos os produtos.
router.get("/", ProductController.index);

// Define uma rota GET para "/showUserProducts" que usa o middleware verifyJwt para verificação de JWT e chama o método showUserProducts do ProductController para listar produtos do usuário autenticado.
router.get("/showUserProducts", verifyJwt, ProductController.showUserProducts);

// Define uma rota GET para "/showRecieverProducts" que usa o middleware verifyJwt para verificação de JWT e chama o método showRecieverProducts do ProductController para listar produtos recebidos pelo usuário autenticado.
router.get("/showRecieverProducts", verifyJwt, ProductController.showRecieverProducts);

// Define uma rota GET para "/:id" que chama o método show do ProductController para exibir os detalhes de um produto específico com base no ID fornecido.
router.get("/:id", ProductController.show);

// Define uma rota PUT para "/:id" que usa middlewares verifyJwt e imageUpload para verificação de JWT e upload de imagens, respectivamente, e chama o método update do ProductController para atualizar um produto específico com base no ID fornecido.
router.put("/:id", verifyJwt, imageUpload.array("images"), ProductController.update);

// Define uma rota DELETE para "/:id" que usa o middleware verifyJwt para verificação de JWT e chama o método delete do ProductController para excluir um produto específico com base no ID fornecido.
router.delete("/:id", verifyJwt, ProductController.delete);

// Define uma rota PATCH para "/schedule/:id" que usa o middleware verifyJwt para verificação de JWT e chama o método schedule do ProductController para agendar uma ação para um produto específico com base no ID fornecido.
router.patch("/schedule/:id", verifyJwt, ProductController.schedule);

// Define uma rota PATCH para "/concludeDonation/:id" que usa o middleware verifyJwt para verificação de JWT e chama o método concludeDonation do ProductController para concluir a doação de um produto específico com base no ID fornecido.
router.patch("/concludeDonation/:id", verifyJwt, ProductController.concludeDonation);


export default router;
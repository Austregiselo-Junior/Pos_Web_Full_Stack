import { Router } from "express";
import { authController } from "../controller/authController.js";

const router = Router();

router.get("/login", authController.login);

export default router;
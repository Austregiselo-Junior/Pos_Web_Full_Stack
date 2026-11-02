import { Router } from "express";
import { UserController } from "../controller/UserController.js";
import { authentication } from "../middleware/authentication.js";

const router = Router();

router.get("/users", authentication, UserController.findAll);
router.get("/users/:username", UserController.findUserByName);
router.post("/users", authentication, UserController.save);

export default router;
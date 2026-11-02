import { sequelize } from "../db/instances/mysql.js";
import { DataTypes } from "sequelize";

export const PostModel = sequelize.define("PostModel",{
    id:{
        type: DataTypes.BIGINT,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    title:{
        type: DataTypes.STRING(80),
        allowNull: false
    },
    user_id:{
        type: DataTypes.BIGINT,
        allowNull:false
    }
},{tableName: "posts"});
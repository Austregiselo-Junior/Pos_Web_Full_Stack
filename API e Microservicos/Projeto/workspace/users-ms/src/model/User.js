import { sequelize } from "../db/instances/mysql.js";
import { DataTypes } from "sequelize";

export const User = sequelize.define("User",{
    id:{
        type: DataTypes.BIGINT,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    username:{
        type: DataTypes.STRING(80),
        allowNull: false
    },
    password:{
        type: DataTypes.STRING(80),
        allowNull:false
    }
},{tableName: "users"});
import Tokenjwt from "jsonwebtoken";

export const authentication = (req, res, next) => {
     const auth = req.headers.authorization;
    try {
        if (!auth) {
            return res.status(401).json({ error: 'Token inválido' });
        }
    } catch (error) {
        res.status(500).json({message: error.message});
    }
    
    const token = auth.split(' ')[1];
    try {
        if (!token) {
            return res.status(401).json({ error: 'Formato do token inválido' });
        }
    } catch (error) {
        res.status(500).json({message: error.message});
    }

  try {
      Tokenjwt.verify(token, process.env.PRIVATE_KEY, (error, decoded) => {
          if (error) {
              return res.status(403).json({ error: 'Token inválido ou expirado' });       
          }
  
          req.user = decoded;
          next();
      });
  } catch (error) {
      res.status(500).json({message: error.message});
  }
};

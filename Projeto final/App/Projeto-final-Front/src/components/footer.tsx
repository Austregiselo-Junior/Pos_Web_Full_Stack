import React from "react";
import { FaFacebook, FaTwitter, FaInstagram } from "react-icons/fa";

const Footer: React.FC = () => {
  return (
    <footer className="bg-dark text-white text-center py-4 mt-auto fixed-bottom">
      <div className="container">
        <p className="mb-1">&copy; 2024 Austregíselo Soares e Thiago Queiroz.</p>
        <div className="d-flex justify-content-center mb-3">
          <a
            href="https://www.facebook.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white mx-3"
          >
            <FaFacebook size={24} />
          </a>
          <a
            href="https://www.twitter.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white mx-3"
          >
            <FaTwitter size={24} />
          </a>
          <a
            href="https://www.instagram.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white mx-3"
          >
            <FaInstagram size={24} />
          </a>
        </div>
        <p className="small mb-0">Todos os direitos reservados.</p>
      </div>
    </footer>
  );
};

export default Footer;

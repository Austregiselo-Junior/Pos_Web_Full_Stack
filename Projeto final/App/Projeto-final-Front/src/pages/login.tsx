import React, { useState } from "react";
import {
  Form,
  Button,
  Card,
  Container,
  InputGroup,
  Row,
  Col,
} from "react-bootstrap";
import { FaUser, FaLock } from "react-icons/fa";
import axios from "axios";
import { useRouter } from "next/router";

interface Usuario {
  usuarioId: number;
  login: string;
  senha: string;
}

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const router = useRouter();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get<Usuario[]>(
        "http://localhost:5228/Usuario"
      );
      const usuarioEncontrado = response.data.find(
        (usuario) => usuario.login === username && usuario.senha === password
      );

      if (usuarioEncontrado) {
        router.push("/paciente");
      } else {
        setError("Usuário ou senha inválidos");
      }
    } catch (error: any) {
      console.error("Erro ao tentar fazer login:", error.message);
      setError(error.message || "Erro inesperado. Tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container
      fluid
      className="d-flex justify-content-center align-items-center vh-100"
      style={{ backgroundColor: "#f0f4f7" }}
    >
      <Row className="w-100">
        <Col
          md={6}
          className="d-flex justify-content-center align-items-center"
        >
          <div
            style={{
              width: "80%",
              height: "80%",
              borderRight: "1px solid rgba(0, 0, 0, 0.1)",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <img
              src="/img/icon.jpeg"
              alt="Imagem"
              style={{
                width: "60%",
                height: "auto",
                borderRadius: "10px",
                boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
              }}
            />
          </div>
        </Col>
        <Col
          md={6}
          className="d-flex justify-content-center align-items-center"
        >
          <Card
            style={{
              width: "22rem",
              borderRadius: "15px",
              boxShadow: "0 8px 16px rgba(0, 0, 0, 0.2)",
              backgroundColor: "#ffffff",
            }}
          >
            <Card.Body>
              <h3 className="text-center mb-4" style={{ color: "#004d7a" }}>
                Login
              </h3>
              {error && <p className="text-danger text-center">{error}</p>}
              <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="username">
                  <Form.Label>Username</Form.Label>
                  <InputGroup>
                    <InputGroup.Text>
                      <FaUser />
                    </InputGroup.Text>
                    <Form.Control
                      type="text"
                      placeholder="Enter username"
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                      required
                    />
                  </InputGroup>
                </Form.Group>
                <Form.Group className="mb-3" controlId="password">
                  <Form.Label>Password</Form.Label>
                  <InputGroup>
                    <InputGroup.Text>
                      <FaLock />
                    </InputGroup.Text>
                    <Form.Control
                      type="password"
                      placeholder="Password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                    />
                  </InputGroup>
                </Form.Group>
                <Button
                  variant="primary"
                  type="submit"
                  className="w-100"
                  disabled={loading}
                  style={{
                    background: "linear-gradient(to right, #004d7a, #00b4db)",
                    border: "none",
                  }}
                >
                  {loading ? "Carregando..." : "Entrar"}
                </Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default LoginPage;

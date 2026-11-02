import React, { useEffect, useState } from "react";
import { Modal, Button, Form, Table } from "react-bootstrap";
import NavBar from "../components/NavBar";
import axios from "axios";
import Footer from "@/components/footer";

interface Paciente {
  clienteId?: number;
  nome: string;
  dataDaConsulta: string;
  telefone: string;
  valorDaSessao?: number;
  categoria?: string;
  quantidadeDeSessao?: number;
  situacaoFinanceira?: string;
  valorPago?: number;
  valorTotal?: number;
  desconto?: number;
  quantidadeParcelas?: number;
  vencimento?: string;
  situacaoFinanceiraMensal?: string;
}

type FormControlElement =
  | HTMLInputElement
  | HTMLSelectElement
  | HTMLTextAreaElement;

const PacientePage: React.FC = () => {
  const [showModalNovoPaciente, setShowModalNovoPaciente] = useState(false);
  const [showModalDetalhesPaciente, setShowModalDetalhesPaciente] =
    useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [pacientes, setPacientes] = useState<Paciente[]>([]);
  const [novoPaciente, setNovoPaciente] = useState<Paciente>({
    nome: "",
    dataDaConsulta: "",
    telefone: "",
    categoria: "Sessão",
    valorDaSessao: 0,
    quantidadeDeSessao: 0,
    valorTotal: 0,
    desconto: 0,
    valorPago: 0,
    vencimento: "",
    situacaoFinanceira: "pago",
  });
  const [pacienteEditando, setPacienteEditando] = useState<Paciente | null>(
    null
  );
  const [editIndex, setEditIndex] = useState<number | null>(null);
  const [pacienteDetalhes, setPacienteDetalhes] = useState<Paciente | null>(
    null
  );

  const fetchPacientes = async () => {
    try {
      const response = await axios.get(
        "http://localhost:5228/Cliente/TabelaDetalhada"
      );
      setPacientes(response.data);
    } catch (error: any) {
      console.error("Erro ao buscar pacientes:", error.message);
    }
  };

  useEffect(() => {
    fetchPacientes();
  }, []);

  const handleInputChange = (e: React.ChangeEvent<FormControlElement>) => {
    const { name, value } = e.target;
    if (pacienteEditando) {
      setPacienteEditando({ ...pacienteEditando, [name]: value });
    } else {
      setNovoPaciente({ ...novoPaciente, [name]: value });
    }
  };

  const handleAddPaciente = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5228/Cliente/AdicionarCliente",
        {
          ...novoPaciente,
          vencimento: novoPaciente.vencimento || "5",
          situacaoFinanceira: novoPaciente.situacaoFinanceira || "pendente",
          dataDoCadastro: new Date().toISOString(),
        }
      );

      console.log("Paciente adicionado:", response.data);
      setShowModalNovoPaciente(false);
      setNovoPaciente({
        nome: "",
        dataDaConsulta: "",
        telefone: "",
        categoria: "Mensal",
      });
      fetchPacientes();
    } catch (error) {
      console.error("Erro ao adicionar paciente:", error);
    }
  };

  const handleEditPaciente = async () => {
    if (!pacienteEditando || !pacienteEditando.clienteId) return;

    try {
      const response = await axios.put(
        `http://localhost:5228/Cliente/AtualizarCliente?id=${pacienteEditando.clienteId}`,
        {
          ...pacienteEditando,
          ultimaAtualizacao: new Date().toISOString(),
        }
      );
      console.log("Paciente atualizado:", response.data);
      setShowEditModal(false);

      setPacienteEditando(null);
      fetchPacientes();
    } catch (error) {
      console.error("Erro ao atualizar paciente:", error);
    }
  };

  const handleDeletePaciente = async (index: number) => {
    const paciente = pacientes[index];
    if (!paciente || !paciente.clienteId) return;

    try {
      await axios.delete(
        `http://localhost:5228/Cliente/RemoverCliente?id=${paciente.clienteId}`
      );
      const updatedPacientes = pacientes.filter((_, i) => i !== index);
      setPacientes(updatedPacientes);
      console.log("Paciente excluído:", paciente.clienteId);
      fetchPacientes();
    } catch (error) {
      console.error("Erro ao excluir paciente:", error);
    }
  };

  const handleEditClick = (paciente: Paciente) => {
    setPacienteEditando(paciente);
    setShowEditModal(true);
  };

  const handleViewDetalhes = (index: number) => {
    setPacienteDetalhes(pacientes[index]);
    setShowModalDetalhesPaciente(true);
  };

  return (
    <div>
      <NavBar />
      <div className="container">
        <div className="d-flex justify-content-between align-items-center mb-4 mt-5">
          <h1 className="text-center flex-grow-1">Pacientes</h1>
          <Button
            variant="success"
            onClick={() => setShowModalNovoPaciente(true)}
          >
            Adicionar Novo Paciente
          </Button>
        </div>

        {/* lista de paciente */}
        <Table striped hover className="mt-4">
          <thead className="bg-info text-white">
            <tr>
              <th>PACIENTE</th>
              <th>TELEFONE PARA CONTATO</th>
              <th>DATA DA CONSULTA</th>
              <th>AÇÕES</th>
            </tr>
          </thead>
          <tbody>
            {pacientes.map((paciente, index) => (
              <tr
                key={index}
                className={`bg-${index % 2 === 0 ? "light" : "white"}`}
              >
                <td>{paciente.nome}</td>
                <td>{paciente.telefone}</td>
                <td>
                  {new Date(paciente.dataDaConsulta).toLocaleDateString(
                    "pt-BR",
                    {
                      day: "2-digit",
                      month: "2-digit",
                      year: "numeric",
                    }
                  )}{" "}
                  às{" "}
                  {new Date(paciente.dataDaConsulta).toLocaleTimeString(
                    "pt-BR",
                    {
                      hour: "2-digit",
                      minute: "2-digit",
                    }
                  )}
                </td>
                <td>
                  <Button
                    variant="info"
                    className="me-2"
                    onClick={() => handleViewDetalhes(index)}
                  >
                    Detalhes
                  </Button>
                  <Button
                    variant="warning"
                    className="me-2"
                    onClick={() => handleEditClick(paciente)}
                  >
                    Editar
                  </Button>
                  <Button
                    variant="danger"
                    onClick={() => handleDeletePaciente(index)}
                  >
                    Deletar
                  </Button>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>

        {/* Modal para Novo Paciente */}
        <Modal
          show={showModalNovoPaciente}
          onHide={() => setShowModalNovoPaciente(false)}
        >
          <Modal.Header closeButton className="bg-info text-white">
            <Modal.Title>Novo Paciente</Modal.Title>
          </Modal.Header>
          <Modal.Body className="bg-light">
            <Form>
              <Form.Group className="mb-3">
                <Form.Label htmlFor="nome">Nome do Paciente</Form.Label>
                <Form.Control
                  type="text"
                  id="nome"
                  name="nome"
                  value={novoPaciente.nome}
                  onChange={handleInputChange}
                />
              </Form.Group>
              <Form.Group className="mb-3">
                <Form.Label htmlFor="dataDaConsulta">
                  Data e Hora da Consulta
                </Form.Label>
                <Form.Control
                  type="datetime-local"
                  id="dataDaConsulta"
                  name="dataDaConsulta"
                  value={novoPaciente.dataDaConsulta}
                  onChange={handleInputChange}
                />
              </Form.Group>
              <Form.Group className="mb-3">
                <Form.Label htmlFor="telefone">
                  Telefone para Contato
                </Form.Label>
                <Form.Control
                  type="tel"
                  id="telefone"
                  name="telefone"
                  value={novoPaciente.telefone}
                  onChange={handleInputChange}
                />
              </Form.Group>
              <Form.Group className="mb-3">
                <Form.Label htmlFor="categoria">Forma de Pagamento</Form.Label>
                <Form.Select
                  id="categoria"
                  name="categoria"
                  value={novoPaciente.categoria}
                  onChange={handleInputChange}
                >
                  <option value="Mensal">Mensal</option>
                  <option value="Sessão">Por Sessão</option>
                </Form.Select>
              </Form.Group>

              {novoPaciente.categoria === "Sessão" && (
                <>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="valorDaSessao">
                      Valor da Sessão
                    </Form.Label>
                    <Form.Control
                      type="number"
                      id="valorDaSessao"
                      name="valorDaSessao"
                      value={novoPaciente.valorDaSessao || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="quantidadeDeSessao">
                      Quantidade de Sessões
                    </Form.Label>
                    <Form.Control
                      type="number"
                      id="quantidadeDeSessao"
                      name="quantidadeDeSessao"
                      value={novoPaciente.quantidadeDeSessao || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="situacaoFinanceira">
                      Situação Financeira
                    </Form.Label>
                    <Form.Control
                      type="text"
                      id="situacaoFinanceira"
                      name="situacaoFinanceira"
                      value={novoPaciente.situacaoFinanceira || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                </>
              )}

              {novoPaciente.categoria === "Mensal" && (
                <>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="desconto">Desconto (%)</Form.Label>
                    <Form.Select
                      id="desconto"
                      name="desconto"
                      value={novoPaciente.desconto || ""}
                      onChange={handleInputChange}
                    >
                      {[...Array(10)].map((_, i) => (
                        <option key={i} value={(i + 1) * 5}>
                          {(i + 1) * 5}%
                        </option>
                      ))}
                    </Form.Select>
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="valorDaSessao">
                      Valor da Sessão
                    </Form.Label>
                    <Form.Control
                      type="number"
                      id="valorDaSessao"
                      name="valorDaSessao"
                      value={novoPaciente.valorDaSessao || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="quantidadeDeSessao">
                      Quantidade de Sessões
                    </Form.Label>
                    <Form.Control
                      type="number"
                      id="quantidadeDeSessao"
                      name="quantidadeDeSessao"
                      value={novoPaciente.quantidadeDeSessao || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="vencimento">
                      Dia de Vencimento
                    </Form.Label>
                    <Form.Control
                      type="number"
                      id="vencimento"
                      name="vencimento"
                      value={novoPaciente.vencimento || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label htmlFor="situacaoFinanceiraMensal">
                      Situação Financeira
                    </Form.Label>
                    <Form.Control
                      type="text"
                      id="situacaoFinanceiraMensal"
                      name="situacaoFinanceiraMensal"
                      value={novoPaciente.situacaoFinanceiraMensal || ""}
                      onChange={handleInputChange}
                    />
                  </Form.Group>
                </>
              )}
            </Form>
          </Modal.Body>
          <Modal.Footer className="bg-light">
            <Button
              variant="secondary"
              onClick={() => setShowModalNovoPaciente(false)}
            >
              Cancelar
            </Button>
            <Button
              variant="warning"
              onClick={() =>
                setNovoPaciente({
                  nome: "",
                  dataDaConsulta: "",
                  telefone: "",
                  categoria: "mensal",
                })
              }
            >
              Limpar
            </Button>
            <Button variant="success" onClick={handleAddPaciente}>
              Adicionar
            </Button>
          </Modal.Footer>
        </Modal>

        {/* Modal de Edição */}
        <Modal show={showEditModal} onHide={() => setShowEditModal(false)}>
          <Modal.Header closeButton className="bg-info text-white">
            <Modal.Title>Editar Paciente</Modal.Title>
          </Modal.Header>
          <Modal.Body className="bg-light">
            {pacienteEditando && (
              <Form>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="edit-nome">Nome do Paciente</Form.Label>
                  <Form.Control
                    type="text"
                    id="edit-nome"
                    name="nome"
                    value={pacienteEditando.nome}
                    onChange={handleInputChange}
                  />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="edit-dataDaConsulta">
                    Data e Hora da Consulta
                  </Form.Label>
                  <Form.Control
                    type="datetime-local"
                    id="edit-dataDaConsulta"
                    name="dataDaConsulta"
                    value={pacienteEditando.dataDaConsulta}
                    onChange={handleInputChange}
                  />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="edit-telefone">
                    Telefone para Contato
                  </Form.Label>
                  <Form.Control
                    type="tel"
                    id="edit-telefone"
                    name="telefone"
                    value={pacienteEditando.telefone}
                    onChange={handleInputChange}
                  />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="edit-categoria">
                    Forma de Pagamento
                  </Form.Label>
                  <Form.Select
                    id="edit-categoria"
                    name="categoria"
                    value={pacienteEditando.categoria}
                    onChange={handleInputChange}
                  >
                    <option value="Mensal">Mensal</option>
                    <option value="Sessão">Por Sessão</option>
                  </Form.Select>
                </Form.Group>

                {pacienteEditando.categoria === "Sessão" && (
                  <>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-valorDaSessao">
                        Valor da Sessão
                      </Form.Label>
                      <Form.Control
                        type="number"
                        id="edit-valorDaSessao"
                        name="valorDaSessao"
                        value={pacienteEditando.valorDaSessao || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-quantidadeDeSessao">
                        Quantidade de Sessões
                      </Form.Label>
                      <Form.Control
                        type="number"
                        id="edit-quantidadeDeSessao"
                        name="quantidadeDeSessao"
                        value={pacienteEditando.quantidadeDeSessao || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-situacaoFinanceira">
                        Situação Financeira
                      </Form.Label>
                      <Form.Control
                        type="text"
                        id="edit-situacaoFinanceira"
                        name="situacaoFinanceira"
                        value={pacienteEditando.situacaoFinanceira || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                  </>
                )}

                {pacienteEditando.categoria === "Mensal" && (
                  <>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-desconto">
                        Desconto (%)
                      </Form.Label>
                      <Form.Select
                        id="edit-desconto"
                        name="desconto"
                        value={pacienteEditando.desconto || ""}
                        onChange={handleInputChange}
                      >
                        {[...Array(10)].map((_, i) => (
                          <option key={i} value={(i + 1) * 5}>
                            {(i + 1) * 5}%
                          </option>
                        ))}
                      </Form.Select>
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="valorDaSessao">
                        Valor da Sessão
                      </Form.Label>
                      <Form.Control
                        type="number"
                        id="valorDaSessao"
                        name="valorDaSessao"
                        value={pacienteEditando.valorDaSessao || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="quantidadeDeSessao">
                        Quantidade de Sessões
                      </Form.Label>
                      <Form.Control
                        type="number"
                        id="quantidadeDeSessao"
                        name="quantidadeDeSessao"
                        value={pacienteEditando.quantidadeDeSessao || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-vencimento">
                        Dia de Vencimento
                      </Form.Label>
                      <Form.Control
                        type="number"
                        id="edit-vencimento"
                        name="vencimento"
                        value={pacienteEditando.vencimento || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                    <Form.Group className="mb-3">
                      <Form.Label htmlFor="edit-situacaoFinanceiraMensal">
                        Situação Financeira
                      </Form.Label>
                      <Form.Control
                        type="text"
                        id="edit-situacaoFinanceiraMensal"
                        name="situacaoFinanceiraMensal"
                        value={pacienteEditando.situacaoFinanceiraMensal || ""}
                        onChange={handleInputChange}
                      />
                    </Form.Group>
                  </>
                )}
              </Form>
            )}
          </Modal.Body>
          <Modal.Footer className="bg-light">
            <Button variant="secondary" onClick={() => setShowEditModal(false)}>
              Cancelar
            </Button>
            <Button variant="success" onClick={handleEditPaciente}>
              Salvar
            </Button>
          </Modal.Footer>
        </Modal>

        {/* Modal para Detalhes do Paciente */}
        {pacienteDetalhes && (
          <Modal
            show={showModalDetalhesPaciente}
            onHide={() => setShowModalDetalhesPaciente(false)}
          >
            <Modal.Header closeButton className="bg-info text-white">
              <Modal.Title>Detalhes do Paciente</Modal.Title>
            </Modal.Header>
            <Modal.Body className="bg-light">
              <p>
                <strong>Nome:</strong> {pacienteDetalhes.nome}
              </p>
              <p>
                <strong>Telefone:</strong> {pacienteDetalhes.telefone}
              </p>
              <p>
                <strong>Data da Consulta:</strong>{" "}
                {new Date(pacienteDetalhes.dataDaConsulta).toLocaleDateString(
                  "pt-BR",
                  {
                    day: "2-digit",
                    month: "2-digit",
                    year: "numeric",
                  }
                )}{" "}
                às{" "}
                {new Date(pacienteDetalhes.dataDaConsulta).toLocaleTimeString(
                  "pt-BR",
                  {
                    hour: "2-digit",
                    minute: "2-digit",
                  }
                )}
              </p>
              <p>
                <strong>Categoria:</strong> {pacienteDetalhes.categoria}
              </p>
              <p>
                <strong>Valor da Sessão:</strong> R${" "}
                {pacienteDetalhes.valorDaSessao}
              </p>
              <p>
                <strong>Quantidade de Sessões:</strong>{" "}
                {pacienteDetalhes.quantidadeDeSessao}
              </p>
              <p>
                <strong>Valor Total:</strong>R$ {pacienteDetalhes.valorTotal}
              </p>
              <p>
                <strong>Desconto:</strong> {pacienteDetalhes.desconto} %
              </p>
              <p>
                <strong>Valor Pago:</strong>R$ {pacienteDetalhes.valorPago}
              </p>
              <p>
                <strong>Dia de Vencimento:</strong>{" "}
                {pacienteDetalhes.vencimento}
              </p>
              <p>
                <strong>Situação Financeira:</strong>{" "}
                {pacienteDetalhes.situacaoFinanceira}
              </p>
            </Modal.Body>
            <Modal.Footer className="bg-light">
              <Button
                variant="secondary"
                onClick={() => setShowModalDetalhesPaciente(false)}
              >
                Fechar
              </Button>
            </Modal.Footer>
          </Modal>
        )}
      </div>
      <Footer />
    </div>
  );
};

export default PacientePage;

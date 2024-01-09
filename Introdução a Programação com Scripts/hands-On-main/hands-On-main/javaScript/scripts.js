const baseUrl = "http://localhost:3000";

// Selecionar os elementos HTML necessários para a "section-Studant"
const studentModal = document.querySelector("#student-modal");
const studentTable = document.querySelector("#student-table");

const studentForm = document.querySelector("#student-form");
const studentModalTitle = document.querySelector("#student-modal-title");

const saveStudentButton = document.querySelector("#save-student");
const cancelStudentButton = document.querySelector("#Cancelar-student");


// Funções para abrir e fechar o modal do estudante
const openStudentModal = () => studentModal.showModal();
const closeStudentModal = () => studentModal.close();

// Func para salvar dados no DB
const saveStundentData = (url, method) => {
  studentForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(studentForm);

    const payload = new URLSearchParams(formData);

    if (Array.from(formData.values()).some((value) => value === "")) {
      alert("Preencha todos os campos corretamente.");
      return;
    }

    fetch(url, {
      method: method,
      body: payload,
    }).catch((error) => {
      closeStudentModal();
      alert("Ocorreu um erro. Tente mais tarde.");
      console.error(error);
    });
  });
};

function updateStundentData(url) {
  studentForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(studentForm);

    const payload = new URLSearchParams(formData);

    if (Array.from(formData.values()).some((value) => value === "")) {
      alert("Preencha todos os campos corretamente.");
      return;
    }
    fetch(url, {
      method: "PUT",
      body: payload,
    }).catch((error) => {
      closeStudentModal();
      alert("Ocorreu um erro. Tente mais tarde.");
      console.error(error);
    });
  });
}

const createStudent = () => {
  saveStundentData(`${baseUrl}/alunos`, "POST");
};

// Passo 4: Criar uma linha na tabela do estudante
const createStudentTableRow = (id, name, matricula, curso) => {
  const tableTr = document.createElement("tr");
  tableTr.innerHTML = `
    <td>${name}</td>
    <td>${matricula}</td>
    <td>${curso}</td>
    <td align="center">
      <button class="button button--danger" onclick="deleteStudentTable(${id})">Apagar</button>
      <button class="button button--success" onclick="editdStudentTable(${id})"}>Editar</button>
    </td>`;
  studentTable.appendChild(tableTr);
};

// Passo 8: Excluir um aluno da tabela
const deleteStudentTable = (id) => {
  fetch(`${baseUrl}/alunos/${id}`, {
    method: "DELETE",
  }).catch((error) => {
    alert("Ocorreu um erro. Tente mais tarde.");
    console.error(error);
  });
};

// Passo 9: Abrir o modal de edição e carregar os dados do aluno
const editdStudentTable = (id) => {
  fetch(`${baseUrl}/alunos/${id}`)
    .then((resp) => resp.json())
    .then((data) => {
      const { nome, matricula, curso } = data;
      studentModalTitle.innerHTML = `Editar Aluno`;
      document.querySelector("#nome").value = nome;
      document.querySelector("#matricula").value = matricula;
      document.querySelector("#curso").value = curso;
      saveStudentButton.innerHTML = "Salvar";

      openStudentModal();

      updateStundentData(`${baseUrl}/alunos/${id}`);
    })
    .catch((error) => {
      alert("Ocorreu um erro. Tente mais tarde.");
      console.error(error);
    });
};

// Passo 10: Chamar a função para carregar dados iniciais da tabela ao carregar a página
const loadStudentTable = async () => {
  try {
    const response = await fetch("http://localhost:3000/alunos");
    const data = await response.json();
    data.forEach((student) => {
      createStudentTableRow(
        student.id,
        student.nome,
        student.matricula,
        student.curso
      );
    });
  } catch (error) {
    alert("Ocorreu um erro. Tente mais tarde.");
    console.error(error);
  }
};

loadStudentTable();

// Selecionar os elementos HTML necessários para a "section-Disciplina"
const disciplinaModal = document.querySelector("#Disciplina-modal");
const disciplinaForm = document.querySelector("#Disciplina-form");
const disciplineModalTitle = document.querySelector("#Disciplina-modal-title")
const saveDisciplineButton = document.querySelector("#save-Discipline");

// Funções para abrir e fechar o modal de disciplina
const openDisciplinaModal = () => disciplinaModal.showModal();
const closeDisciplinaModal = () => disciplinaModal.close();

const saveDisciplinaData = (url, method) => {
  disciplinaForm.addEventListener("submit", (event) => {
    event.preventDefault();

    // capturar os dados do formulário
    const formData = new FormData(disciplinaForm);

    if (Array.from(formData.values()).some((value) => value === "")) {
      alert("Preencha todos os campos corretamente.");
      return;
    }

    // transformar os dados do formulário em um objeto
    const payloadURL = new URLSearchParams(formData);

    fetch(url, {
      method: method,
      body: payloadURL,
    }).catch((error) => {
      closeStudentModal();
      alert("Não foi possível salvar a disciplina. Tente mais tarde.");
      console.error(error);
    });
  });
};

function updateDisciplinaData(url) {
  studentForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(disciplinaForm);

    const payload = new URLSearchParams(formData);

    if (Array.from(formData.values()).some((value) => value === "")) {
      alert("Preencha todos os campos corretamente.");
      return;
    }
    fetch(url, {
      method: "PUT",
      body: payload,
    }).catch((error) => {
      closeStudentModal();
      alert("Ocorreu um erro. Tente mais tarde.");
      console.error(error);
    });
  });
}

const addDisciplina = () => {
  saveDisciplinaData(`${baseUrl}/disciplinas`, "POST");
};

const createDisciplineTableRow = (id, nome, cargaHoraria, NomeProfessor, curso, ObservacoesDisciplina) => {
  const tableTr = document.createElement("div");
  tableTr.classList.add("subject-card");
  tableTr.innerHTML =
    `<h3 class="subject-card__title">${nome}</h3>
    <hr />
    <ul class="subject-card__list">
      <li>Carga horária: ${cargaHoraria}</li>
      <li>Professor: ${NomeProfessor}</li>
      <li>Status <span class="tag ${curso === "Obrigatória" ? "tag--danger" : "tag--success"
    }">${curso}</span></li>
      <li>Observações: ${ObservacoesDisciplina}</li>
    </ul>
    
    <div class="subject-card__actions">
      <button class="button button--danger" onclick="deleteDisciplineCard(${id})">Apagar</button>
      <button class="button button--success" onclick="editedDisciplineCard(${id})"}>Editar</button>    
    </div>`;

  document.querySelector(".Cards").appendChild(tableTr);
};

const deleteDisciplineCard = (id) => {
  fetch(`${baseUrl}/disciplinas/${id}`, {
    method: "DELETE",
  }).catch((error) => {
    alert("Não foi possível deletar a disciplina", id, ".", "Tente mais tarde.");
    console.error(error);
  });
};

const editedDisciplineCard = (id) => {
  fetch(`${baseUrl}/disciplinas/${id}`)
    .then((resp) => resp.json())
    .then((data) => {
      console.error(data);
      const { nome, cargaHoraria, NomeProfessor, curso, ObservacoesDisciplina } = data;
      disciplineModalTitle.innerHTML = `Editar Disciplina' "${nome}"`;
      document.querySelector("#nomeDisciplina").value = nome;
      document.querySelector("#CargaHorariaDisciplina").value = cargaHoraria;
      document.querySelector("#NomeProfessordaDisciplina").value = NomeProfessor;
      document.querySelector("#StatusDisciplina").value = curso;
      document.querySelector("#ObservacoesDisciplina").value = ObservacoesDisciplina;
      saveDisciplineButton.innerHTML = "Salvar";
      openDisciplinaModal();
      updateDisciplinaData(`${baseUrl}/disciplinas/${id}`);
    })
    .catch((error) => {
      alert("Não foi possível editar a disciplina");
      console.error(error);
      console.log(error);
    });
};

const loadDisciplinasTable = async () => {
  try {
    const response = await fetch(`${baseUrl}/disciplinas`);
    const data = await response.json();
    data.forEach((discipline) => {
      createDisciplineTableRow(discipline.id, discipline.nome, discipline.cargaHoraria, discipline.NomeProfessor, discipline.curso, discipline.ObservacoesDisciplina);
    });
  } catch (error) {
    alert("Não foi possível carregar as disciplinas. Tente mais tarde.");
    console.error(error);
  }
};

loadDisciplinasTable();



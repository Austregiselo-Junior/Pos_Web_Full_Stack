// Etapa 0
// pega todos os elementos do accordion-header já que vamos clicar neles
const header = document.querySelectorAll(".accordion-header");
const accordionItems = document.querySelectorAll('.accordion-item')
// Etapa 1
// Adiciona evento de click em todos os headers e bota o console.log

// console.log(header)

header.forEach((header) => {
  console.log(header)
  header.addEventListener('click', () => {
    const item = header.parentNode
    const isActive = item.classList.contains('accordion-item--active')
    console.log(isActive)

    console.log(!isActive)
    // console.log('item', item)
    // console.log('isActive', isActive)

    accordionItems.forEach((item) => {
      item.classList.remove('accordion-item--active')
      item.classList.add('accordion-item--closed');
    })

    if(!isActive) {
      item.classList.add('accordion-item--active');
      item.classList.remove('accordion-item--closed')
    }
  })
});

// Etapa 4
// verifica se esta ativo para adicionar e remover as classes
// Etapa 5
// para cada item remve e adiciona classe de ativo e fechado

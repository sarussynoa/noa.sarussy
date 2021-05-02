console.log(`Js loaded`)

function toggleModal(e) {
  e.preventDefault()
  let popup = document.getElementById('popup');
  if (popup) {
    popup.classList.toggle('show')
  }
}
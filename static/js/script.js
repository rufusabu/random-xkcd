console.log("JS WOrks");

const reloadButton = document.querySelector(".btn");

const nextImg = () => {
  window.location.reload();
};

reloadButton.addEventListener("click", nextImg);
document.addEventListener("keyup", event => {
  if (event.keyCode === 13) {
    nextImg();
  }
});

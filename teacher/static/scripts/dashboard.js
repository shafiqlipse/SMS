// sidebar scripts

const sidebar = document.querySelector(".sidebar");
const Ntext = document.querySelectorAll(".nav-text");

// const dropbtn = document.querySelectorAll(".fa-chevron-right ");

const Shrink = () => {
  Ntext.forEach((text) => {
    text.style.display = "none";
  });
  sidebar.style.flex = "0 0 50px";
};

const Shrunk = () => {
  Ntext.forEach((text) => {
    text.style.display = "inline";
  });
  sidebar.style.flex = "0 0 250px";
};

// accordion
const navlinks = document.querySelectorAll(".navlink");
const navlists = document.querySelectorAll(".navlist");

navlinks.forEach((navlink) => {
  navlink.addEventListener("click", () => {
    content = navlink.nextElementSibling;
    content.style.display = content.style.display === "flex" ? "none" : "flex";
    console.log(content.style);
  });

  // console.log(list.classList);
});

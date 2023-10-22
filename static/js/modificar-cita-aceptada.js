const citaCumplidaTrue = document.getElementById("cita-cumplida-true");
const citaCumplidaFalse = document.getElementById("cita-cumplida-false");
const motivoAusencia = document.getElementById("motivo-ausencia");

if (citaCumplidaFalse.checked) {
  motivoAusencia.style.height = motivoAusencia.scrollHeight + "px";
}

citaCumplidaFalse.addEventListener("click", () => {
  motivoAusencia.style.height = motivoAusencia.scrollHeight + "px";
});

citaCumplidaTrue.addEventListener("click", () => {
  motivoAusencia.style.height = 0;
});
document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const toggleSidebar = document.getElementById("toggleSidebar");
  const overlay = document.getElementById("overlay");
  const toggleIcon = document.getElementById("toggleIcon");
  const toggleMaster = document.getElementById("toggle-master");
  const togglePeriode = document.getElementById("toggle-periode");
  const submenu = document.getElementById("submenu");
  const submenu2 = document.getElementById("submenu2");

  // Sidebar show/hide for mobile
  toggleSidebar.addEventListener("click", function () {
    sidebar.classList.toggle("-translate-x-full");
    overlay.classList.toggle("hidden");
    toggleIcon.classList.toggle("fa-bars");
    toggleIcon.classList.toggle("fa-times"); // Toggle between hamburger and X icon
  });

  // Close sidebar when clicking on overlay
  overlay.addEventListener("click", function () {
    sidebar.classList.add("-translate-x-full");
    overlay.classList.add("hidden");
    toggleIcon.classList.remove("fa-times");
    toggleIcon.classList.add("fa-bars"); // Change icon back to hamburger
  });

  // Master Karyawan submenu toggle with smooth transition
  toggleMaster.addEventListener("click", function () {
    submenu.classList.toggle("hidden");
    submenu.classList.toggle("transition-all");
    submenu.classList.toggle("duration-500");
    toggleChevron(toggleMaster);
  });

  // Periode Berjalan submenu toggle with smooth transition
  togglePeriode.addEventListener("click", function () {
    submenu2.classList.toggle("hidden");
    submenu2.classList.toggle("transition-all");
    submenu2.classList.toggle("duration-500");
    toggleChevron(togglePeriode);
  });

  function toggleChevron(element) {
    const img = element.querySelector("img");
    img.classList.toggle("rotate-90");
    img.classList.toggle("rotate-0");
  }
});

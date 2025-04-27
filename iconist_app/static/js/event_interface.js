function master_Karyawan() {
    var submenu = document.getElementById("submenu");
    var chevron = document.querySelector(".chevron-icon");

    // Toggle the display of the submenu
    if (submenu.style.display === "block") {
        submenu.style.display = "none";
        chevron.classList.remove("rotate");
    } else {
        submenu.style.display = "block";
        chevron.classList.add("rotate");
    }
}

function kont_skor() {
    var submenu = document.getElementById("submenu2");
    var chevron = document.querySelector(".chevron-icon2");

    // Toggle the display of the submenu
    if (submenu.style.display === "block") {
        submenu.style.display = "none";
        chevron.classList.remove("rotate");
    } else {
        submenu.style.display = "block";
        chevron.classList.add("rotate");
    }
}

// Untuk sidebar
function open_submenu() {
    var submenu = document.getElementById("submenu");
    submenu.style.display = "block";
    // PR open_submenu tidak bisa karena ketika di klik otomatis style value direset karena open tab baru
}


// function modal_data_Karyawan() {
//     // Get the modal
//     var modal = document.getElementById("pop-up");

//     // Get the button that opens the modal
//     var btn = document.getElementById("button_tambah_data");

//     // Get the <span> element that closes the modal
//     var span = document.getElementById("close_modal_data_Karyawan");

//     // When the user clicks the button, open the modal 
//     btn.onclick = function () {
//         modal.style.display = "block";
//     }

//     // When the user clicks on <span> (x), close the modal
//     span.onclick = function () {
//         modal.style.display = "none";
//     }

//     // When the user clicks anywhere outside of the modal, close it
//     window.onclick = function (event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     }
// }

function modal_import_data_Karyawan() {
    var modal = document.getElementById("import_data");
    var overlay = document.getElementById("modal_import_data_Karyawan");
    overlay.style.display = "block";
    modal.classList.add("active");
}

function close_import_modal_data_Karyawan() {
    var overlay = document.getElementById("modal_import_data_Karyawan");
    overlay.style.display = "none";
}


function modal_add_Karyawan() {
    var modal = document.getElementById("add_data");
    var overlay = document.getElementById("modal_tambah_data_Karyawan");;
    overlay.style.display = "block";
    modal.classList.add("active");
}

function close_add_data_Karyawan() {
    var overlay = document.getElementById("modal_tambah_data_Karyawan");
    overlay.style.display = "none";
}


function modal_hapus_Karyawan() {
    var modal = document.getElementById("hapus_data");
    var overlay = document.getElementById("modal_hapus_data_Karyawan");;
    overlay.style.display = "block";
    modal.classList.add("active");
}

function close_hapus_data_Karyawan() {
    var overlay = document.getElementById("modal_hapus_data_Karyawan");
    overlay.style.display = "none";
}

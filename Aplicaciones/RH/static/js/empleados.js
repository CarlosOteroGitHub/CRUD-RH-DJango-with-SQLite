/* FUNCIÓN JAVASCRIPT PARA PREGUNTAR ANTES DE ELIMINAR UN REGISTRO */

(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el empleado?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();
// Forza lo scroll della pagina all'inizio ogni volta che viene ricaricata o quando si lascia la pagina e la si riapre dopo
window.onbeforeunload = function () {
    window.scrollTo(0, 0);
};
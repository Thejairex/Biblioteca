const changeStyle = (x) => {
    link = document.getElementById('estilo')

    if (x == 1) {
        link.href = '/static/css/bootstrap.min.css'
    } else if (x == 2) {
        link.href = '/static/css/bootstrap.min.dark.css'
    } else if (x == 3) {
        link.href = '/static/css/bootstrap.min.neon.css'
    } else if (x == 4) {
        link.href = '/static/css/bootstrap.min.quartz.css'
    }
    

}

let dropdowns = document.getElementById('dropdown-main')
dropdowns.addEventListener('click', function (e) {
        var el = this.nextElementSibling
        el.style.display = el.style.display==='block'?'none':'block'
    })
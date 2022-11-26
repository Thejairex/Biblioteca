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

const changeStar = (item) => {
    console.log(item.id);
    let contador = item.id;

    for (let i = 0; i < 5; i++) {
        if (i<contador) {
            document.getElementById(i+1).style.color="orange";
        } else {
            document.getElementById(i+1).style.color="black";
        }
        
    }
}

let dropdowns = document.getElementById('dropdown-main')
dropdowns.addEventListener('click', function (e) {
        var el = this.nextElementSibling
        el.style.display = el.style.display==='block'?'none':'block'
    })
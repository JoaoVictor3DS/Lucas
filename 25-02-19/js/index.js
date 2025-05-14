function list() {
    document.getElementById('list').innerHTML +=
        `<li>${document.getElementById('input').value}
        <button class="list_item">X</button></li>`;

    document.getElementById('input').value = '';
}
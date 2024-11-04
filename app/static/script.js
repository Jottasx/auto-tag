const file_input = document.getElementById("file_input");
const btn_product = document.getElementById("btn_load_product");
const btn_sasoi006 = document.getElementById("btn_send_to_sasoi006");
const btn_tagsell = document.getElementById("btn_send_to_tagsell");
const btn_clear = document.getElementById("btn_products_clear")


// Evento para abrir o seletor de arquivos
btn_product.addEventListener("click", () => {
    file_input.click();
});

btn_clear.addEventListener("click", () => {
    fetch("/clear_products", {
        method: 'GET',
    }).then(() => {
        window.location.reload()
    })
    
});

// Evento para carregar e processar o arquivo selecionado
file_input.addEventListener("change", () => {
    const file = file_input.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("file", file);

        fetch("/", {
            method: 'POST',
            body: formData
        })
        .then(() => {
            window.location.reload()
        })
        .catch(error => {
            console.error("Erro ao carregar dados:", error);
        });
        
    } else {
        console.log("Nenhum arquivo selecionado");
    }
});


const file_input = document.getElementById("file_input");
const select_all = document.getElementById("select_all")
const btn_product = document.getElementById("btn_load_product");
const btn_sasoi006 = document.getElementById("btn_send_to_sasoi006");
const btn_tagsell = document.getElementById("btn_send_to_tagsell");
const btn_clear = document.getElementById("btn_products_clear")

// Função para auxiliar a verificação de quais inputs estão selecionados na tabela
function is_one_checked_at_least() {
    const inputs = document.querySelectorAll("input[type='checkbox']")
    const checked_products = []
    inputs.forEach((input) => {
        if (input.checked && input.getAttribute("id") != "select_all") {
            checked_products.push(
                {
                    ['product_code']: input.getAttribute("id")
                }
            )
        }
    })

    return checked_products
}

// Evento para selecionar todos os checkbox a partir do principal
select_all.addEventListener("click", () => {
    inputs = document.querySelectorAll("input[type='checkbox']")
    inputs.forEach((input) => {
        if (input.getAttribute("id") != "select_all") {
            input.checked = select_all.checked
        }
    })
})

// Evento para abrir o seletor de arquivos
btn_product.addEventListener("click", () => {
    file_input.click();
});

// Evento para limpar os produtos do banco de dados e da tabela
btn_clear.addEventListener("click", () => {
    fetch("/clear_products", {
        method: 'GET',
    }).then(() => {
        window.location.reload()
    })
    
});

// Evento para enviar os produtos para o Save Web tela SASOI006
btn_sasoi006.addEventListener("click", () => {
    const checked_products = is_one_checked_at_least()
    if (checked_products.length == 0) {
        alert("Nenhum produto foi selecionado, por favor selecione pelo menos um produto")
        return
    }

    open_sasoi_modal()
    
})

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

// Função para abrir o modal
function open_sasoi_modal() {
    document.getElementById('modal_sasoi').classList.add('show');
}

// Função para fechar o modal
function close_sasoi_modal() {
    document.getElementById('modal_sasoi').classList.remove('show');
}

function send_to_sasoi006() {
    const login = document.getElementById("sw-login");
    const password = document.getElementById("sw-password");
    const filial = document.getElementById("sw-filial");

    if (login.value.length > 0 && password.value.length > 0 && filial.value.length > 0) {
        const checked_products = is_one_checked_at_least(); 

        fetch("/call_sasoi006", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user_data: {
                    login: login.value,
                    password: password.value,
                    filial: filial.value
                },
                checked_products
            })
        })
        .then((res) => res.json())
        .then((data) => {
            //window.location.reload()
        })
        .catch((error) => {
            console.error("Erro na requisição:", error);
        });
    } else {
        console.log("Todos os campos precisam estar preenchidos.");
    }
}

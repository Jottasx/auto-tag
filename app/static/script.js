const file_input = document.getElementById("file_input");
const select_all = document.getElementById("select_all")
const btn_product = document.getElementById("btn_load_product");
const btn_sasoi006 = document.getElementById("btn_send_to_sasoi006");
const btn_tagsell = document.getElementById("btn_send_to_tagsell");
const btn_clear = document.getElementById("btn_products_clear")
const html_console = document.getElementById("console")

// Função para auxiliar a verificação de quais inputs estão selecionados na tabela
function get_checked_products() {
    const inputs = document.querySelectorAll("input[type='checkbox']")
    const checked_products = []
    inputs.forEach((input) => {
        if (input.checked && input.getAttribute("id") != "select_all") {
            checked_products.push(
                {
                    ["product_code"]: input.getAttribute("id")
                }
            )
        }
    })

    return checked_products
}

window.onload = function() {
    if (!sessionStorage.logs) {
        sessionStorage.setItem("logs", `[OK] [${new Date().toLocaleTimeString()}] - Sistema iniciado com sucesso! <br>`)
    }

    
    html_console.innerHTML += sessionStorage.getItem("logs")
    html_console.scrollTop = html_console.scrollHeight
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
        method: "GET",
    }).then(() => {
        updateConsole("OK", "Lista de protudos foi esvaziada")
        window.location.reload()
    })
    
});

// Evento para enviar os produtos para o Save Web tela SASOI006
btn_sasoi006.addEventListener("click", () => {
    const checked_products = get_checked_products()
    if (checked_products.length == 0) {
        open_warning_modal("Selecione ao menos 1 produto para enviar para o Save Web")
        return
    }

    open_sasoi_modal()
      
    
})

// Evento para enviar os produtos para o TagSell
btn_tagsell.addEventListener("click", () => {

    const checked_products = get_checked_products()

    if (checked_products.length == 0) {
        open_warning_modal("Selecione pelo menos 1 produto")
        return
    }

    open_tagsell_modal()

    
})

// Evento para carregar e processar o arquivo selecionado
file_input.addEventListener("change", () => {
    const file = file_input.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("file", file);

        fetch("/", {
            method: "POST",
            body: formData
        })
        .then(() => {
            updateConsole("OK", "Produtos carregados com sucesso")
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
    document.getElementById("modal_sasoi").classList.add("show");
}

function open_tagsell_modal() {
    document.getElementById("modal_tagsell").classList.add("show");
}

// Função para fechar o modal
function close_sasoi_modal() {
    document.getElementById("modal_sasoi").classList.remove("show");
}

function close_tagsell_modal() {
    document.getElementById("modal_tagsell").classList.remove("show");
}

function open_warning_modal(message) {
    document.getElementById("modal_footer").classList.remove("modal-footer")
    document.getElementById("modal_footer").classList.add("modal-footer-center")
    document.getElementById("modal_body").innerHTML = message
    document.getElementById("modal_warning").classList.add("show");
}

function close_warning_modal() {
    document.getElementById("modal_warning").classList.remove("show");
}

function send_to_sasoi006() {
    const login = document.getElementById("sw-login");
    const password = document.getElementById("sw-password");
    const filial = document.getElementById("sw-filial");

    if (login.value.length > 0 && password.value.length > 0 && filial.value.length > 0) {
        const checked_products = get_checked_products(); 
        
        close_sasoi_modal()

        updateConsole(".....", "Enviando produtos para o SAVE WEB (SASOI006) aguarde...")

        fetch("/call_sasoi006", {
            method: "POST",
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
        .then((res) => {
            return res.json()
        })
        .then((data) => {
            if (data.msg == "Credenciais Inválidas") {
                updateConsole("ER", "Credenciais inválidas ou bloqueio do usuário, tente novamente mais tarde")
                return
            }

            updateConsole("OK", "Produto(s) ENVIADOS para o SAVEWEB (SASOI006)")
            window.location.reload()
        })
    } else {
        updateConsole("ER", "Campos inválidos")
    }
}

function send_to_tagsell() {
    const login = document.getElementById("ts-login");
    const password = document.getElementById("ts-password");

    if (login.value.length > 0 && password.value.length > 0) {
        const checked_products = get_checked_products(); 
        
        close_tagsell_modal()

        updateConsole(".....", "Enviando produtos para o Tag Sell (RASCUNHO) aguarde...")

        fetch("/call_tagsell", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user_data: {
                    login: login.value,
                    password: password.value,
                },
                checked_products
            })
        })
        .then(() => {
            updateConsole("OK", "Produto(s) ENVIADOS para o Tag Sell (RASCUNHO)")
            
        })
    } else {
        updateConsole("ER", "Campos inválidos")
    }
}

function updateConsole(status, info) {
    let now = new Date().toLocaleTimeString()
   
    logs = sessionStorage.getItem("logs") || ""
    const new_log = `[${status}] [${now}] - ${info} <br>`

    logs += new_log

    sessionStorage.setItem("logs", logs)

    html_console.innerHTML += sessionStorage.getItem("logs")
    html_console.scrollTop = html_console.scrollHeight

}
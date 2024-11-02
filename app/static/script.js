const file_input = document.getElementById("file_input");
const table = document.getElementById("table");
const btn_product = document.getElementById("btn_load_product");

let products = [];
let decoded_product = [];

// Configurando o Proxy para observar alterações no array products
products = new Proxy(products, {
    set: (target, prop, value) => {
        const result = Reflect.set(target, prop, value);
        updateTable(); // Atualiza a tabela ao alterar o array
        return result;
    }
});

// Função para atualizar a lista de produtos
function updateProducts(product_list) {
    product_list.forEach(product => {
        products.push(product); // Adiciona cada produto ao array observado
    });
}

// Função para atualizar a tabela
function updateTable() {
    // Limpa as linhas existentes na tabela
    table.innerHTML = `
        <tr>
            <th><input type="checkbox" id="select_all" /></th>
            <th>COD</th>
            <th>Desc</th>
            <th>Emb</th>
            <th>Preço</th>
            <th>Local</th>
            <th>Status</th>
        </tr>
    `;

    // Adiciona cada produto como uma nova linha na tabela
    for (let i = 0; i < products.length; i++) {
        let row = table.insertRow(-1);

        let cell_1 = row.insertCell(0);
        let cell_2 = row.insertCell(1);
        let cell_3 = row.insertCell(2);
        let cell_4 = row.insertCell(3);
        let cell_5 = row.insertCell(4);
        let cell_6 = row.insertCell(5);
        let cell_7 = row.insertCell(6);

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";

        cell_1.append(checkbox);
        cell_2.innerText = products[i]._Product__code;
        cell_3.innerText = products[i]._Product__descritpion;
        cell_4.innerText = products[i]._Product__emb;
        cell_5.innerText = `$R$ ${products[i]._Product__price}`.replace('.', ',');
        cell_6.innerText = products[i]._Product__local;
        cell_7.innerText = products[i]._Product__status;
    }

    document.getElementById("select_all").addEventListener("click", (event) => {
        const inputs = table.querySelectorAll("input[type='checkbox']");
        inputs.forEach(element => {
            element.checked = event.target.checked; // Marca ou desmarca todos os checkboxes
        });
    });
}

// Evento para abrir o seletor de arquivos
btn_product.addEventListener("click", () => {
    file_input.click();
});

// Evento para carregar e processar o arquivo selecionado
file_input.addEventListener("change", () => {
    const file = file_input.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("file", file);

        fetch("/load-excel", {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            decoded_product = data.products.map(product => JSON.parse(product));
            updateProducts(decoded_product); // Atualiza o array products, que chama updateTable
        })
        .catch(error => {
            console.error("Erro ao carregar dados:", error);
        });
    } else {
        console.log("Nenhum arquivo selecionado");
    }
});


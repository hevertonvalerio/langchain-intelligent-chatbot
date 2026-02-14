from langchain_core.documents import Document

documentos_empresa = [
    Document(
        page_content="Política de férias: Funcionários têm direito a 30 dias de férias após 12 meses. A solicitação deve ser feita com 30 dias de antecedência.",
        metadata={"tipo": "política", "departamento": "RH", "ano": 2024, "id_doc": "doc001"}
    ),

    Document(
        page_content="Processo de reembolso de despesas: Envie a nota fiscal pelo portal financeiro. O reembolso ocorre em até 5 dias úteis.",
        metadata={"tipo": "processo", "departamento": "Financeiro", "ano": 2023, "id_doc": "doc002"}
    ),

    Document(
        page_content="Guia de TI: Para configurar a VPN, acesse vpn.nossaempresa.com e siga as instruções para seu sistema operacional.",
        metadata={"tipo": "tutorial", "departamento": "TI", "ano": 2024, "id_doc": "doc003"}
    ),

    Document(
        page_content="Código de Ética e Conduta: Valorizamos o respeito, a integridade e a colaboração. Casos de assédio não serão tolerados.",
        metadata={"tipo": "política", "departamento": "RH", "ano": 2022, "id_doc": "doc004"}
    )

]
     
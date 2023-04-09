<h1>Santo do Dia</h1>
<p>Este projeto é um aplicativo muito bom e eficaz para encontrar o Santo do Dia e exibi-lo em uma janela pop-up no computador. Ele foi projetado para ajudar os usuários a se conectar com a fé e se inspirar nos santos que são lembrados e comemorados a cada dia.</p>

<h2>Tecnologias e Conceitos</h2>
<ul>
    <li>Python</li>
    <li>Web scraping com a biblioteca BeautifulSoup</li>
    <li>Beautiful Soup</li>
    <li>Construindo uma interface gráfica do usuário (GUI) usando a biblioteca PySimpleGUI</li>
    <li>Enviando solicitações HTTP usando Requests</li>
    <li>Expressões regulares (regex) com o módulo re</li>
    <li>Tempfile</li>
</ul>

<h2>Como funciona</h2>
<p>O aplicativo utiliza a biblioteca <code>requests</code> para fazer uma solicitação HTTP ao site <code>https://santo.cancaonova.com/</code>. Em seguida, a biblioteca <code>BeautifulSoup</code> é usada para analisar o conteúdo HTML da página e extrair informações relevantes, como o nome do santo, a imagem, a legenda da imagem e a descrição.</p>
<p>A função <code>get_saint_of_the_day()</code> é responsável por todo o processo de busca e exibição das informações. O aplicativo utiliza <code>PySimpleGUI</code> para criar e exibir uma janela pop-up com as informações extraídas, incluindo uma imagem do santo e a descrição.</p>

<h2>Exemplo</h2>
<p>A janela pop-up exibirá informações detalhadas sobre o Santo do Dia, incluindo:</p>
<ul>
    <li>Data atual</li>
    <li>Nome do santo</li>
    <li>Imagem do santo</li>
    <li>Legenda da imagem</li>
    <li>Descrição do santo</li>
</ul>
<p align="center">
  <img src="https://i.imgur.com/VJtVc4n.jpeg" width="350" title="hover text">
  <img src="https://i.imgur.com/EaN9s6l.png" width="350" alt="accessibility text">
</p>

<h2>Modificações e aplicações úteis</h2>
<p>Este projeto pode ser adaptado para diversas aplicações. Algumas modificações possíveis incluem:</p>
<ul>
    <li>Scraping para exibição de outros conteúdos diários, como citações, horóscopos, eventos históricos ou até mesmo a previsão do tempo.</li>
    <li>Expandir o aplicativo para incluir informações adicionais, como orações, leituras ou reflexões.</li>
    <li>Integrar o aplicativo com outros serviços, como calendários ou gerenciadores de tarefas, para fornecer lembretes ou notificações.</li>
    <li>Criar uma versão de aplicativo da web do aplicativo usando uma estrutura da web como Flask ou Django, tornando-a acessível a partir de um navegador.</li>
</ul>

<h2>Contribuição</h2>
<p>Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue no GitHub ou enviar um pull request com suas sugestões e melhorias. Por favor, siga as diretrizes de contribuição e o código de conduta do projeto.</p>

<h2>Licença</h2>
<p>Este projeto está licenciado sob a <a href="https://opensource.org/licenses/MIT">Licença MIT</a>, que permite uso, cópia, modificação, mesclagem

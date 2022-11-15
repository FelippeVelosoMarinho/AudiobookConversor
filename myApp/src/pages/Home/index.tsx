import { useEffect } from "react";

import '../../App.css';
import './style.css';

function Home() {

  useEffect(() => {
    document.title = "Home | Audiobook Conversor";
  });

  return (
    <div className='App'>
            <div className="cabeçalho">
              
              <div className="logo">
                  <img src="https://i.imgur.com/9Q1Z1Zu.png" alt="logo" />
              </div>

              <div className="dropdown">
                  <button className="dropbtn">Início</button>
                  <div className="dropdown-content">
                  <a href="."></a>
                  </div>
              </div>
            
            </div>
            <div className="conteudo">
              <h2 >Transforme seu arquivo PDF em audio</h2>
              <h4>Ainda em fase de testes :/</h4>
              <button className="dropbtn2">Selecionar arquivo PDF</button>
            </div>

    </div>
  );
}

export default Home;
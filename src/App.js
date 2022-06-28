import React, {useState, useEffect} from 'react';

import './App.css';
import './script';

function App() {
  return (
    <div>
    <div className="start_btn"><button>Start Quiz</button></div>
    <div className="info_box">
      <div className="info-title"><span>Rules Game</span></div>
      <div className="info-list">
        <div className="info">1. Avrai 15 secondi di tempo ad ogni risposta!<span /> </div>
        <div className="info">2. Usa il tuo sapere non consultare Internet!</div>
        <div className="info">3. Alla fine del Quiz potrai consultare il risulato!!</div>
        <div className="info">5. Se fai piu di 5 errori è meglio che approfondisci la tua coltura :(</div>
      </div>
      <div className="buttons">
        <button className="quit">Exit Quiz</button>
        <button className="restart">Continue</button>
      </div>
    </div>
    <div className="quiz_box">
      <header>
        <div className="title">Awesome Quiz Application</div>
        <div className="timer">
          <div className="time_left_txt">Time Left</div>
          <div className="timer_sec">15</div>
        </div>
        <div className="time_line" />
      </header>
      <section>
        <div className="que_text">
        </div>
        <div className="option_list">
        </div>
      </section>
      <footer>
        <div className="total_que">
        </div>
        <button id="next-question" className="next_btn">Next Question</button>
      </footer>
    </div>
    <div className="result_box">
      <div className="icon">
        <i className="fas fa-crown" />
      </div>
      <div className="complete_text">You've completed the Quiz!</div>
      <div className="score_text">
        -&gt;
      </div>
      <div className="buttons">
        <button className="restart">Replay Quiz</button>
        <button className="quit">Quit Quiz</button>
      </div>
    </div>
    <footer>
      <div id="form">
        <form>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">Email:</label>
            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
            <br />
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputPassword1" className="form-label">Password:</label>
            <input type="password" className="form-control" id="exampleInputPassword1" />
          </div>
          <div><button id="btn" type="submit" className="btn btn-primary">Submit</button></div>
        </form>
      </div>
    </footer>
  </div>
);
}



export default App;



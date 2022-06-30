import axios from 'axios';

import './App.css';
import './script';

import React, { useState, useEffect } from 'react';

export default function App() {


	const questions = [
		{
			questionText: 'Quale città ha più abitanti?',
			answerOptions: [
				{ answerText: 'New York', isCorrect: false },
				{ answerText: 'Pechino', isCorrect: false },
				{ answerText: 'New Dheli', isCorrect: true },
				{ answerText: 'Tokyo', isCorrect: false },
			],
		},
		{
			questionText: 'Quali sono i colori sociali di Roma?',
			answerOptions: [
				{ answerText: 'Bianco e Celeste', isCorrect: false },
				{ answerText: 'Giallo e Rosso', isCorrect: true },
				{ answerText: 'Giallo e Blu', isCorrect: false },
				{ answerText: 'Bianco e Giallo', isCorrect: false },
			],
		},
		{
			questionText: 'Quale animale gloglotta?',
			answerOptions: [
				{ answerText: 'Tacchino', isCorrect: true },
				{ answerText: 'Passerotto', isCorrect: false },
				{ answerText: 'Cane', isCorrect: false },
				{ answerText: 'Maiale', isCorrect: false },
			],
		},
		{
			questionText: 'In che anno è stata scoperta lAmerica',
			answerOptions: [
				{ answerText: '1512', isCorrect: false },
				{ answerText: '1500', isCorrect: false },
				{ answerText: '1489', isCorrect: false },
				{ answerText: '1492', isCorrect: true },
			],
		},
    {
			questionText: 'Quale tra le seguenti nazionali ha vinto 5 mondiali?',
			answerOptions: [
				{ answerText: 'Italia', isCorrect: false },
				{ answerText: 'Brasile', isCorrect: true },
				{ answerText: 'Francia', isCorrect: false },
				{ answerText: 'Inghilterra', isCorrect: false },
			],
		},
    {
			questionText: 'La Bandiera di quale nazione non ha una forma rettangolare',
			answerOptions: [
				{ answerText: 'St.Kitts & Nevis', isCorrect: false },
				{ answerText: 'Nepal', isCorrect: true },
				{ answerText: 'Isole Vergini Britanniche ', isCorrect: false },
				{ answerText: 'Taipei', isCorrect: false },
			],
		},
    {
			questionText: 'Quando è finita la Seconda Guerra Mondiale',
			answerOptions: [
				{ answerText: '1943', isCorrect: false },
				{ answerText: '1945', isCorrect: true },
				{ answerText: '1944', isCorrect: false },
				{ answerText: '1946', isCorrect: false },
			],
		},
    {
			questionText: 'Quali città furono colpite dalla bomba atomica?',
			answerOptions: [
				{ answerText: ' Sapporo e Sendai', isCorrect: false },
				{ answerText: ' Hiroshima e Nagasaki', isCorrect: true },
				{ answerText: ' Kyoto e Nagoya', isCorrect: false },
				{ answerText: 'Kumamoto e Sagamihara ', isCorrect: false },
			],
		},
    {
			questionText: 'Quale tra le seguenti nazionali ha vinto 5 mondiali?',
			answerOptions: [
				{ answerText: ' ', isCorrect: false },
				{ answerText: ' ', isCorrect: true },
				{ answerText: ' ', isCorrect: false },
				{ answerText: ' ', isCorrect: false },
			],
		},
    {
			questionText: 'Quale tra le seguenti nazionali ha vinto 5 mondiali?',
			answerOptions: [
				{ answerText: ' ', isCorrect: false },
				{ answerText: ' ', isCorrect: true },
				{ answerText: ' ', isCorrect: false },
				{ answerText: ' ', isCorrect: false },
			],
		},
	];

	const [currentQuestion, setCurrentQuestion] = useState(0);
	const [showScore, setShowScore] = useState(false);
	const [score, setScore] = useState(0);
	const [back, setBack] = useState([])
	useEffect(()=>{
		axios.get("http://127.0.0.1:8000/user").then(
			res=>{
				console.log(res)
				setBack(res.data)
			}
			
		).catch(err=>{
			console.log(err)
		})
	})

	const handleAnswerOptionClick = (isCorrect) => {
		if (isCorrect) {
			setScore(score + 1);
		}

		const nextQuestion = currentQuestion + 1;
		if (nextQuestion < questions.length) {
			setCurrentQuestion(nextQuestion);
		} else {
			setShowScore(true);
		}
	};
	
	  return (
  		
  		<div>
  		    <div className='app'>
      			{showScore ? (
      				<div className='score-section'>
      					You scored {score} out of {questions.length}
      				</div>
      			) : (
      				<>
      					<div className='question-section'>
      						<div className='question-count'>
      							<span>Question {currentQuestion + 1}</span>/{questions.length}
      						</div>
      						<div className='question-text'>{questions[currentQuestion].questionText}</div>
      					</div>
      					<div className='answer-section'>
      						{questions[currentQuestion].answerOptions.map((answerOption) => (
      							<button onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}>{answerOption.answerText}</button>
      						))}
      					</div>
      				</>
      			)}
            
  		  </div>
        
       <footer>
        <div id="form">
          <form>
            <div className="mb-3">
              <label htmlFor="exampleInputEmail1" className="form-label">Username:</label>
              <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
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
);}
import React from 'react';
import '../../styles/Game.css';

const Game = ({ gameTime, teamA, teamB, odds }) => {
  return (
    <div className="game">
      <div className="game-time">Game Time: {gameTime}</div>
      <div className="teams">Teams: {teamA} vs {teamB}</div>
      <div className="odds">Odds of Team A Winning: {odds}</div>
    </div>
  );
};

export default Game;

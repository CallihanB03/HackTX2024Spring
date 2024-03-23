import React from 'react';

const Game = ({ gameTime, teamA, teamB, oddsOfTeamA }) => {
  return (
    <div>
      <p>Game Time: {gameTime}</p>
      <p>Teams: {teamA} vs {teamB}</p>
      <p>Odds of Team A Winning: {oddsOfTeamA}</p>
    </div>
  );
};

export default Game;

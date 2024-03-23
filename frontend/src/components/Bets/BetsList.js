import React from 'react';
import Game from './Game';

const BetsList = ({ games }) => {
  return (
    <div>
      {games.map((game, index) => (
        <Game
          key={index}
          gameTime={game.gameTime}
          teamA={game.teamA}
          teamB={game.teamB}
          odds={game.odds}
        />
      ))}
    </div>
  );
};

export default BetsList;
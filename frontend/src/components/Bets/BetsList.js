import React from 'react';
import Game from './Game';
import React from 'react';
import Game from './Game';

const BetsList = () => {
  return (
    <div>
      <Game gameTime="12:00 PM" teamA="Team A" teamB="Team B" oddsOfTeamA="2.5" />
      <Game gameTime="3:00 PM" teamA="Team C" teamB="Team D" oddsOfTeamA="1.8" />
      <Game gameTime="6:00 PM" teamA="Team E" teamB="Team F" oddsOfTeamA="3.2" />
    </div>
  );
};

export default BetsList;
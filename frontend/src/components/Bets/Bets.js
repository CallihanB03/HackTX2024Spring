import React from 'react';
import BetsList from './BetsList';

function Bets() {
  return (
    <div>
      <h1>Current Bets</h1>
      <div>
        <BetsList />
        <p>
          Text under the list of bets
        </p>
      </div>
      
    </div>
  );
}

export default Bets;
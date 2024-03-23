import React, { useEffect, useState } from 'react';
import BetsList from './BetsList';

function Bets() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/bets');
      const data = await response.json();
      setGames(data);
    } catch (error) {
      console.error('Error fetching games:', error);
    }
  };

  // Temporary games array
  const tempGames = [
    { id: 1, name: 'Game 1', gameTime: '12:00 PM', teamA: 'Dallas Mavs', teamB: 'GS Warriors', odds: -100 },
    { id: 2, name: 'Game 2', gameTime: '3:00 PM', teamA: 'Team C', teamB: 'Team D', odds: +200 },
    { id: 3, name: 'Game 3', gameTime: '6:00 PM', teamA: 'Team E', teamB: 'Team F', odds: +300 }
  ];

  return (
    <div>
      <h1>Current Bets</h1>
      <div>
        <BetsList games={games.length > 0 ? games : tempGames} />
        <p>
          Text under the list of bets
        </p>
      </div>
    </div>
  );
}

export default Bets;
// Bets.js
import React, { useEffect, useState } from 'react';
import BetsList from './BetsList';
import { Container, Typography } from '@mui/material';

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

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Current Bets
      </Typography>
      <BetsList games={games.length > 0 ? games : []} />
    </Container>
  );
}

export default Bets;

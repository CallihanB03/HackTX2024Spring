// Game.js
import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const Game = ({ gameTime, teamA, teamB, odds }) => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h6">Game Time: {gameTime}</Typography>
        <Typography>Teams: {teamA} vs {teamB}</Typography>
        <Typography>Odds of Team A Winning: {odds}</Typography>
      </CardContent>
    </Card>
  );
};

export default Game;

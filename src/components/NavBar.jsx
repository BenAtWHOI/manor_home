import React, { useState } from 'react'
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import './NavBar.css'

const Navbar2 = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const [menuIndex, setMenuIndex] = useState(null);

  const handleClick = (event, index) => {
    setAnchorEl(event.currentTarget);
    setMenuIndex(index);
  };

  const handleClose = () => {
    setAnchorEl(null);
    setMenuIndex(null);
  };

  const menus = [
    { title: 'Atlantis', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Atlantis Data at DLA', 'Cruise Synopsis'] },
    { title: 'Armstrong', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Armstrong Data at DLA', 'Cruise Synopsis'] },
    { title: 'Tioga', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Tioga Data at DLA', 'Cruise Synopsis'] },
    { title: 'Miscellaneous', items: ['The Ships', 'Ship Tracker', 'Ship Schedules', 'Woods Hole Weather'] },
  ];

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h5" sx={{ flexGrow: 1 }}>
          Manor
        </Typography>
        {menus.map((menu, index) => (
          <div key={index} className='dropdown'>
            <Button
              aria-controls={`menu-${index}`}
              aria-haspopup="true"
              onClick={(event) => handleClick(event, index)}
              style={{color: 'white'}}
            >
              <h3>{menu.title}</h3>
            </Button>
            <Menu
              id={`menu-${index}`}
              anchorEl={anchorEl}
              keepMounted
              open={Boolean(anchorEl) && menuIndex === index}
              onClose={handleClose}
            >
              {menu.items.map((item, i) => (
                <MenuItem key={i} onClick={handleClose}>
                  {item}
                </MenuItem>
              ))}
            </Menu>
          </div>
        ))}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar2;


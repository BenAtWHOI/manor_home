import React, { useState, useEffect, useRef } from 'react'
import AppBar from '@mui/material/AppBar'
import Button from '@mui/material/Button'
import Toolbar from '@mui/material/Toolbar'
import './NavBar.css'

const Navbar = () => {
  const [openMenuIndex, setOpenMenuIndex] = useState(null)
  const menuRefs = useRef([])

  const handleToggleMenu = (index) => {
    setOpenMenuIndex(openMenuIndex === index ? null : index)
  }

  const handleCloseMenu = () => {
    setOpenMenuIndex(null)
  }

  const handleClickOutside = (event) => {
    if (menuRefs.current.every(ref => ref && !ref.contains(event.target))) {
      handleCloseMenu()
    }
  }

  useEffect(() => {
    document.addEventListener('click', handleClickOutside)
    return () => {
      document.removeEventListener('click', handleClickOutside)
    }
  }, [])

  const menus = [
    { title: 'Atlantis', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Atlantis Data at DLA', 'Cruise Synopsis'] },
    { title: 'Armstrong', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Armstrong Data at DLA', 'Cruise Synopsis'] },
    { title: 'Tioga', items: ['Ship Information', 'Underway Data', 'Plot Data', 'Wiki (Replica)', 'ACDP Plots', 'Tioga Data at DLA', 'Cruise Synopsis'] },
    { title: 'Miscellaneous', items: ['The Ships', 'Ship Tracker', 'Ship Schedules', 'Woods Hole Weather'] },
  ]

  return (
    <AppBar position="static">
      <Toolbar sx={{ backgroundColor: '#041E42', height: '15vh' }}>
        <img src='https://www.whoi.edu/wp-content/uploads/2022/01/WHOI_PrimaryWhiteType%C2%AE.png' alt='WHOI Logo' style={{ 'width': '15vw' }} />
        <span style={{width: '30vw'}}></span>
        {menus.map((menu, index) => (
          <div key={index} className='dropdown' ref={el => menuRefs.current[index] = el}>
            <Button
              aria-haspopup="true"
              onClick={() => handleToggleMenu(index)}
              style={{ color: 'white' }}
            >
              <h3>{menu.title}</h3>
            </Button>
            {openMenuIndex === index && (
              <ul className="dropdown-menu">
                {menu.items.map((item, idx) => (
                  <li key={idx} onClick={handleCloseMenu}>{item}</li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </Toolbar>
    </AppBar>
  );
}

export default Navbar

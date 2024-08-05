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
        {
            title: 'Atlantis',
            items: [
                { name: 'Ship Information', url: 'http://www.whoi.edu/main/ships/atlantis' },
                { name: 'Underway Data', url: 'https://manor.whoi.edu/cgi-bin/db_driven_data/update_screen.pl?ship=atlantis' },
                { name: 'Plot Data', url: 'https://manor.whoi.edu/atlantis.xy' },
                { name: 'Wiki (Replica)', url: 'https://manor.whoi.edu/atlantis_dokuwiki/doku.php' },
                { name: 'ACDP Plots', url: 'http://currents.soest.hawaii.edu/uhdas_fromships/atlantis/figs/' },
                { name: 'Atlantis Data at DLA', url: 'http://dlacruisedata.whoi.edu/AT/cruise/' },
                { name: 'Cruise Synopsis', url: 'http://www.whoi.edu/page.do?pid=156936' }
            ]
        },
        { 
            title: 'Armstrong', 
            items: [
                {name: 'Ship Information', url: 'http://www.whoi.edu/main/ships/neil-armstrong'}, 
                {name: 'Underway Data', url: 'https://manor.whoi.edu/cgi-bin/db_driven_data/update_screen.pl?ship=armstrong'}, 
                {name: 'Plot Data', url: 'https://manor.whoi.edu/armstrong.xy'}, 
                {name: 'Wiki (Replica)', url: 'https://manor.whoi.edu/armstrong_dokuwiki/doku.php'}, 
                {name: 'ACDP Plots', url: 'http://currents.soest.hawaii.edu/uhdas_fromships/armstrong/figs/'}, 
                {name: 'Armstrong Data at DLA', url: 'http://dlacruisedata.whoi.edu/AR/cruise/'}, 
                {name: 'Cruise Synopsis', url: 'http://www.whoi.edu/page.do?pid=156956'}
            ] 
        },
        { 
            title: 'Tioga', 
            items: [
            {name: 'Ship Information', url:'http://www.whoi.edu/main/ships/tioga'}, 
            {name: 'Underway Data', url:'https://manor.whoi.edu/cgi-bin/db_driven_data/update_screen.pl?ship=tioga'}, 
            {name: 'Plot Data', url:'https://manor.whoi.edu/tioga.xy'}, 
            {name: 'ACDP Plots', url:'http://currents.soest.hawaii.edu/uhdas_fromships/tioga/figs/'}, 
            {name: 'Tioga Data at DLA', url:'https://www.dla.whoi.edu/cruises/tioga'}, 
            {name: 'Cruise Synopsis', url:'http://www.whoi.edu/page.do?pid=160577'},
            {name: 'Tioga Cruises 2010-2018', url:'http://sssg1.whoi.edu/tioga/tioga_cruises.html'}

        ] 

        },
        { 
            title: 'Miscellaneous', 
            items: [
            {name: 'The Ships', url: 'http://www.whoi.edu/main/ships'}, 
            {name: 'Ship Tracker', url: 'https://www.whoi.edu/what-we-do/explore/ships/ship-tracker/'}, 
            {name: 'Ship Schedules', url: 'https://www.whoi.edu/what-we-do/explore/ships/ships-schedules/'}, 
            {name: 'Woods Hole Weather', url: 'http://woodsholeweather.org/'}

        ] 

        },
    ]

    return (
        <AppBar position="static">
            <Toolbar sx={{ backgroundColor: '#041E42', height: '15vh' }}>
                <img src='https://www.whoi.edu/wp-content/uploads/2022/01/WHOI_PrimaryWhiteType%C2%AE.png' alt='WHOI Logo' style={{ 'width': '15vw' }} />
                <span style={{ width: '30vw' }}></span>
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
                                    <li key={idx} onClick={handleCloseMenu}>
                                        <a href={item.url} style={{ color: 'inherit', textDecoration: 'none' }}>
                                            {item.name}
                                        </a>
                                    </li>
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

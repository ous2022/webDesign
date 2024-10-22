import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import axios from 'axios'

const Connexion = () => {


    const [mail, setMail] = useState('')
    const [pwd, setPwd] = useState('')

    const handleMail = (e) => {
        setMail(e.target.value)
    } 
    
    const handlePwd = (e) => {
        setPwd(e.target.value)
    }

    const submitFom = (e) => {
        e.preventDefault()
        console.log(mail, pwd)
        axios.post('http://localhost:3001/api/auth/login', {
            email: mail,
            password: pwd
        })
        setPwd('')
        setMail('')
    }


    return( 
        <div className='connect'>
            <div className="left">
                <h1>Connexion</h1>
                <p>
                    Connectez-vous ici pour acceder à notre site dans son integralité
                </p>

                <form onSubmit={submitFom}>
                    <div className="email">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" name="email" value={mail} onChange={handleMail} />
                    </div>
                    <div className="password">
                        <label htmlFor="password">Mot de passe</label>
                        <input type="password" id="password" name="password" value={pwd} onChange={handlePwd} />
                    </div>

                    <div className="btn">
                        <button type="submit">Se connecter</button>
                    </div>
                </form>
                <span>
                    Vous n'avez pas de compte ? <Link className="toco" to="/inscription">Inscrivez vous</Link>
                </span>
            </div>

            <div className="right">
                <img src="" alt="" />
            </div>
        </div>
    )
}

export default Connexion
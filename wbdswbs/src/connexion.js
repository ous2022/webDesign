import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import axios from 'axios'

const Connexion = () => {


    const [mail_client, setMail] = useState('')
    const [mot_de_passe, setPwd] = useState('')

    const handleMail = (e) => {
        setMail(e.target.value)
    } 
    
    const handlePwd = (e) => {
        setPwd(e.target.value)
    }

    const submitFom = (e) => {
        e.preventDefault()
        console.log(mail, pwd)
        axios.post('http://127.0.0.1:8000/api/connexion/', {
            email: mail,
            password: pwd
        }).then(res => {
            console.log(res.data)
        }).catch(error => {
            console.log('Vous avez une erreur dans votre code' ,error)
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
                        <input type="email" id="email" name="email" value={mail_client} onChange={handleMail} />
                    </div>
                    <div className="password">
                        <label htmlFor="password">Mot de passe</label>
                        <input type="password" id="password" name="password" value={mot_de_passe} onChange={handlePwd} />
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
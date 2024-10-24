import axios from "axios"
import { useState } from "react"
import { Link } from "react-router-dom"

const Inscription = () => {

    const [nom_complet, setName] = useState('')
    const [mail_client, setMail] = useState('')
    const [numero_de_telephone, setNumber] = useState('')
    const [mot_de_passe, setPassword] = useState('')


    const handleName = (e) => {
        setName(e.target.value)
    }

    const handleMail = (e) => {
        setMail(e.target.value)
    }

    const handleNumber = (e) => {
        setNumber(e.target.value)
    }

    const handlePassword = (e) => {
        setPassword(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()

        axios.post('http://127.0.0.1:8000/api/inscription', {
            nom: nom_complet,
            email: mail_client,
            numero: numero_de_telephone,
            password: mot_de_passe,
        }).then(res => {
            console.log(res.data)
        }).catch(err => {
            console.log('Encore une erreur mon petit', err)
        })

        setName('')
        setMail('')
        setNumber('')
        setPassword('')
    }


    return(
        <div className="connect">
            <div className="left">
                <h1>Inscription</h1>
                <p>
                    Inscrivez-vous ici pour acceder à notre site dans son integralité
                </p>

                <form onSubmit={handleSubmit}>
                    <div className="nom">
                        <label htmlFor="nom">Nom Complet</label>
                        <input type="nom" id="nom" name="nom" value={nom_complet} onChange={handleName} />
                    </div>
                    <div className="email">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" name="email " value={mail_client} onChange={handleMail} />
                    </div>
                    <div className="numero">
                        <label htmlFor="numero">Numero de telephone</label>
                        <input type="tel" id="numero" name="numero" value={numero_de_telephone} onChange={handleNumber} />
                    </div>
                    <div className="password">
                        <label htmlFor="password">Mot de passe</label>
                        <input type="password" id="password" name="password" value={mot_de_passe} onChange={handlePassword} />
                    </div>

                    <div className="btn">
                        <button type="submit">S'inscrire</button>
                    </div>
                </form>
                <span>
                    Vous avez déjà un compte ? <Link className="toco" to="/connexion">Connectez vous</Link>
                </span>
            </div>

            <div className="right">
                <img src="" alt="" />
            </div>

        </div>
    )
}

export default Inscription
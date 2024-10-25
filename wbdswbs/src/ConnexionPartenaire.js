import { useState } from "react"
import { Link } from "react-router-dom"
import axios from 'axios'

const ConnexionPartenaire = () => {

    // const [code, setCode] = useState('')
    const [mail, setMail] = useState('')
    const [pwd, setPwd] = useState('')

    /* const handleCode = (e) => {
        setCode(e.target.value)
    } */

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
            // code: code,
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
                    Connectez-vous ici pour pour pouvoir ajouter des articles au panier
                </p>

                <form onSubmit={submitFom}>
                    {/* <div className="code">
                        <label htmlFor="code">Code</label>
                        <input type="text" id="code" name="code" value={code} onChange={handleCode} />
                    </div> */}
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
                <p>Vous êtes un partenaire ou un intermediaire ?<Link className="toco" to="/connexionPartenaire">Cliquez ici</Link></p>
            </div>

            <div className="right">
                <img src="" alt="" />
            </div>
        </div>
    )
}

export default ConnexionPartenaire
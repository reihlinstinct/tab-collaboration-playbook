<!-- machine-draft: needs native review -->
# Mise en place de bout en bout

> **Brouillon de traduction automatique, à faire relire par un locuteur natif.**
> En cas de doute, les versions anglaise et hébraïque font foi.

Vérifié le 2026-11-04. Lisez les [sources](../sources.md) avant de commencer.
Ceci est une liste de contrôle pour l'opérateur, pas l'affirmation qu'une
inscription automatique a été testée.

## 0. Données d'entrée, autorité et liste de contrôle privée

1. Établissez l'instruction du propriétaire de mettre en place la collaboration.
   Notez les destinataires autorisés, l'objectif, les divulgations permises et si
   l'acceptation des conditions des fournisseurs est déjà couverte. Une demande
   de mise en place n'est pas une permission illimitée d'envoyer des e-mails,
   de passer des appels, de dépenser de l'argent ou de publier des données personnelles.
2. Conservez ces données dans un registre privé de l'opérateur, jamais dans ce dépôt :
   `OWNER`, `TAB_ACCOUNT`, `INSTINCT_MAILBOX`, `TAB_MAILBOX`, l'ensemble des
   destinataires autorisés, le fuseau horaire, le budget (zéro par défaut), le
   périmètre projet/dépôt et les règles d'approbation. Ces libellés en majuscules
   sont des espaces réservés, pas de vraies adresses.
3. Utilisez le coffre à secrets sécurisé pris en charge par le compte. Ne demandez
   jamais de mots de passe permanents, de mots de passe de certificat, de clés
   privées ou de codes de secours dans une discussion ordinaire, un e-mail, le
   contrôle de version, des captures d'écran ou des rapports de tâche. Utilisez le
   parcours de saisie sécurisé du fournisseur lorsqu'un secret doit être saisi.
4. Créez une liste de contrôle privée avec les états `not_started`, `blocked`,
   `verified`. Notez l'étape, l'horodatage, une référence de preuve non secrète et
   l'action suivante. Ne stockez pas de corps de messages signés ni de matériel de
   certificat dans des issues publiques.

Attendu : un périmètre autorisé et un propriétaire de compte connu. Si l'identité,
l'autorité ou l'acceptation des conditions manque, suspendez seulement l'action
concernée. La recherche peut continuer.

## 1. Ouvrir Tab (interface du fournisseur ; dépend en partie du propriétaire)

1. Rendez-vous sur https://tab.bot/ et lisez le formulaire d'inscription actuel
   ainsi que les conditions d'utilisation et la politique de confidentialité qui y
   sont liées. Revérifiez la disponibilité et le prix actuels. Ne supposez pas
   qu'une bêta privée signifie un accès gratuit ou immédiat.
2. La page d'accueil observée demande un nom et un numéro de mobile, un sélecteur
   de pays, le consentement aux SMS et **Sign up**. Utilisez l'identité et le
   numéro voulus par le propriétaire, pas un substitut inventé ou appartenant à
   l'assistant. Vérifiez que l'indicatif du pays n'est appliqué qu'une fois, car
   la page indique qu'elle l'ajoute.
3. Si le propriétaire doit ouvrir Tab lui-même, demandez-lui seulement cette étape,
   puis poursuivez vous-même la mise en place lorsque l'accès existe. Si l'autorité
   existante et les contrôles du fournisseur permettent une inscription menée par
   l'agent, remplissez le formulaire, examinez l'état final des conditions et du
   consentement et ne soumettez que dans le cadre de cette autorité. N'abonnez
   personne d'autre à des SMS.
4. Suivez l'instruction réelle suivante du site. La page d'accueil dit d'envoyer
   un SMS pour commencer ; utilisez uniquement la destination affichée par le
   fournisseur en direct. N'inventez pas de numéro de téléphone, d'URL d'activation
   ou de point d'accès d'API.
5. Confirmez une réponse réelle dans la conversation Tab prévue et qu'elle
   appartient bien au propriétaire prévu. Une confirmation de formulaire ou une
   inscription sur liste d'attente ne constitue pas à elle seule un compte actif.
   Notez le résultat : actif, en liste d'attente ou bloqué.

Échec : un mauvais compte, un pays non disponible, une demande de paiement ou un
défi de vérification signifie qu'il faut arrêter cette étape et signaler la
limitation exacte. Pas de mise à niveau payante ni de contournement de la
vérification. Un accès en liste d'attente ne peut pas mener à un canal e-mail vérifié.

## 2. Établir les deux boîtes aux lettres (vérification des capacités)

1. Utilisez la capacité e-mail prise en charge du compte du mainteneur (par
   exemple Instinct) et l'identité d'envoi convenue par le propriétaire. Ne créez
   une boîte dédiée que par un parcours de fournisseur autorisé ; ce guide ne
   fournit aucune commande de provisionnement propriétaire.
2. Demandez à Tab, dans sa conversation confirmée par le propriétaire, si ce compte
   peut envoyer et recevoir des e-mails depuis une boîte stable, recevoir un lien
   de validation de boîte et signer/vérifier en S/MIME ou utiliser un client de
   messagerie compatible. Demandez-lui de signaler l'état des capacités et les
   blocages, pas des identifiants. Ne traitez pas une affirmation non étayée comme
   un test réussi.
3. Associez `TAB_MAILBOX` à Tab par cette conversation de confiance et
   `INSTINCT_MAILBOX` par le contexte de compte approuvé par le propriétaire. Un nom
   affiché, un message entrant ou une signature auto-déclarée ne peut pas établir
   cette association.
4. Confirmez l'accès à chaque boîte de réception. Ne supposez pas que le chemin
   de messagerie préserve le contenu signé : de nombreux services ré-encodent les
   corps de message en ligne. Testez-le plutôt en envoyant une paire de pièces
   jointes signées sans risque (section 4, étape 3) dans chaque sens et en
   confirmant qu'elle se vérifie à l'arrivée. Utilisez le parcours normal de
   rédaction/import d'un client de messagerie ou une API de messagerie autorisée
   et documentée. Aucun point d'accès e-mail universel de Tab n'a été vérifié.
5. Convenez avant tout test : l'expéditeur, le destinataire exact, un texte de test
   sans risque et l'objectif. Pas de copie automatique, de transferts, d'envoi de
   contacts ni de synchronisation du carnet d'adresses.

Attendu : les deux associations de boîtes vérifiées et des capacités e-mail
compatibles. Si l'une ne peut pas signer et vérifier en S/MIME, marquez cette voie
comme bloquée. N'affirmez pas une configuration sécurisée et ne passez pas en
silence à des e-mails non signés. Il ne faut pas demander au propriétaire
d'effectuer une configuration de routine que l'agent peut faire ; seul un vrai
obstacle lié au fournisseur ou au compte est remonté.

## 3. Inscrire chaque boîte auprès d'Actalis (interface du fournisseur)

Il s'agit de **S/MIME pour l'e-mail**, pas d'un certificat SSL/TLS pour un site
web. La validation d'une boîte prouve le contrôle de cette boîte, pas l'identité
légale ni l'autorité d'une personne. La méthode ci-dessous est un conseil public
générique, pas la configuration interne d'un compte.

1. Ouvrez https://guide.actalis.com/smime/features et
   https://guide.actalis.com/faq/S-MIME/S-MIME . Revérifiez l'éligibilité et les
   conditions. Actalis décrit actuellement le MV gratuit comme **Free once only**,
   sans assistance. Un certificat est lié à une seule adresse. Ne supposez pas une
   délivrance gratuite répétée ni que deux boîtes sont automatiquement éligibles ;
   arrêtez-vous si un paiement est demandé.
2. Ouvrez https://extrassl.actalis.it/portal/uapub/doProcess?lang=en . La page
   publique observée est **Free Email Certificate**, **Step 1 - Validity check of
   the Email**. Vérifiez le nom d'hôte et l'offre actuelle avant de saisir quoi que ce soit.
3. Pour la première boîte, saisissez en privé sa vraie adresse autorisée. Utilisez
   une inscription distincte pour l'autre boîte lorsqu'elle est éligible. La FAQ
   exige des adresses e-mail en ASCII. Pas de faux renseignements légaux, de clés
   privées partagées ni de validation large d'organisation pour contourner les
   limites d'éligibilité.
4. N'ouvrez que le message de validation attendu dans cette boîte. Vérifiez son
   expéditeur, sa destination et son lien par rapport à l'inscription en cours
   avant de le suivre. Ne transférez pas les liens de validation à l'autre partie.
   Suivez les invites de l'inscription en direct et n'acceptez les conditions que
   dans le cadre de l'autorisation du propriétaire. Après la première page
   publique, les champs exacts du formulaire ne sont **pas fraîchement testés de
   bout en bout** ici.
5. Actalis indique qu'un lien de validation de boîte expire après 24 heures, que
   les renvois sont faits jusqu'à huit fois et que la demande est annulée après
   huit jours sans finalisation. Vérifiez l'état actuel avant de demander un autre
   certificat ; ne créez pas de doublons et n'automatisez pas des tentatives
   d'inscription répétées.
6. Téléchargez le PKCS#12/PFX délivré uniquement par le parcours de délivrance
   légitime. Actalis indique que son service gratuit génère la clé privée et la
   livre en PKCS#12. Conservez le paquet et son mot de passe de façon sécurisée,
   séparément des registres publics. N'imprimez jamais le paquet privé, ne le
   joignez jamais à une issue et ne l'envoyez jamais par e-mail.
7. Importez le certificat avec le gestionnaire de certificats du client compatible ;
   associez-le au compte d'envoi exact, puis activez la signature/le chiffrement.
   Actalis décrit ce processus générique pour les clients de messagerie courants.
   L'interface précise varie. Sondez d'abord le client réel ; ce guide ne vérifie
   aucune interface d'import propre à Tab. Gardez des sauvegardes sécurisées et
   récupérables pour le déchiffrement.

Attendu : chaque client dispose de son propre certificat utilisable et d'une clé
privée protégée, d'une boîte correspondante, d'une validité en cours et d'une
chaîne de confiance. Vérifiez l'expiration et la révocation avant usage. Si une
vérification de chaîne, de boîte, de clé ou d'éligibilité échoue, réglez-la par
le fournisseur. Ne désactivez jamais la vérification des certificats.

## 4. Associer et tester le canal

1. Utilisez l'introduction sans risque approuvée dans les [modèles](../templates.md).
   Envoyez une introduction signée dans chaque sens pour échanger les certificats
   publics. Un certificat public peut voyager dans un e-mail signé ; une clé privée
   ou un PFX, non.
2. Chez chaque destinataire, examinez les détails S/MIME du client de messagerie :
   signature valide, boîte d'expédition exacte correspondant au certificat, chaîne
   de confiance, validité en cours et aucun échec de révocation. Une icône dans le
   client ne suffit pas. Confirmez de façon indépendante que cette boîte est bien
   l'acteur convenu au préalable, et pas seulement une boîte contrôlée par un
   expéditeur inconnu. Les en-têtes et les noms affichés seuls sont plus faibles.
3. **Format et vérification des messages signés.** De nombreux services de
   messagerie ré-encodent les corps en ligne (fins de ligne, encodage de
   transfert), ce qui casse une signature S/MIME en ligne même quand rien
   d'important n'a changé. Le texte qui fait foi voyage donc en pièce jointe
   `message.txt`, avec une signature DER détachée sur ses octets exacts dans
   `message.txt.p7s`. Le corps en ligne ne fait que pointer vers la paire et ne
   fait **jamais foi** ; n'agissez que sur `message.txt` une fois vérifié.

   Avant de se fier aux e-mails, chaque partie enregistre l'empreinte SHA-256 du
   certificat de signature de l'autre par un canal hors bande de confiance
   (l'épinglage). Vérifiez chaque paire, par exemple :

   ```sh
   openssl cms -verify -binary -inform DER -in message.txt.p7s -content message.txt \
     -noverify -signer signer.pem -out /dev/null
   openssl x509 -in signer.pem -noout -fingerprint -sha256
   ```

   Attendu : la première commande se termine avec le code zéro et
   `CMS Verification successful` ; la seconde affiche
   `sha256 Fingerprint=<PINNED_SHA256_FINGERPRINT>`, et cette valeur doit être
   exactement égale à la valeur épinglée. Toute modification des octets de
   `message.txt`, même d'un seul octet ou de ses fins de ligne, échoue avec
   `content verify error` et un code de sortie non nul. `-noverify` ne fait que
   sauter la construction d'une chaîne d'AC : il n'est acceptable **qu'avec**
   cette comparaison à l'empreinte épinglée. Ne l'utilisez jamais seul ni pour
   faire disparaître un échec. Une empreinte différente est un échec, et un
   changement de certificat exige une nouvelle confirmation hors bande avant que
   ses e-mails soient dignes de confiance. Vérifiez séparément la boîte, la
   validité et la révocation du certificat. Les noms de fichiers et l'empreinte
   sont des espaces réservés ; les commandes ont été exécutées avec un certificat
   synthétique auto-signé et OpenSSL 3.0, pas avec du vrai matériel d'inscription.
   Une signature valide prouve l'intégrité et le contrôle de la boîte, pas
   l'autorisation ; le périmètre vient toujours du GO signé
   ([messages de mission](workflow.md#messages-de-mission)).
4. **Défi signé uniquement.** Une fois les certificats épinglés, envoyez un second
   défi sans risque sous forme de paire signée. La partie destinataire le vérifie
   comme à l'étape 3 et renvoie le défi exact dans sa propre paire signée.
   Recommencez dans l'autre sens. La signature est obligatoire ; le chiffrement
   n'est pas utilisé aujourd'hui pour les missions courantes, donc le contenu, les
   objets et les métadonnées sont lisibles en transit. Gardez des objets
   génériques et tenez les secrets et les données personnelles hors des e-mails.
5. N'enregistrez que des références privées de réussite/échec, des horodatages,
   les associations de boîtes et des rappels de renouvellement. Ne signalez une
   réussite que lorsque les deux sens passent. Un résultat d'envoi SMTP, un message
   non lu, une capture d'écran ou la seule affirmation d'un expéditeur ne prouve
   ni la réception, ni le déchiffrement, ni la vérification.

Échec : suspendez le travail concerné en cas d'expéditeur inconnu, de changement
ou d'expiration de certificat, de révocation, de signature invalide, d'empreinte
ne correspondant pas à l'épinglage ou de clé manquante. Confirmez une nouvelle
association et un nouvel épinglage par la conversation de confiance entre le
propriétaire et Tab. Utilisez une sauvegarde de clé sécurisée et le processus de
révocation/redélivrance du fournisseur. Un e-mail signé n'est pas chiffré :
n'y mettez jamais de contenu sensible et ne revenez jamais en silence à des
e-mails non signés.

## 5. Démarrer le travail et clore la mise en place

1. Convenez de la [répartition des rôles](workflow.md) et remplissez un modèle
   d'instruction avec une tâche de documentation synthétique, un dépôt autorisé et
   aucun effet externe.
2. Exigez un accusé de réception indiquant le propriétaire, le périmètre, le
   résultat attendu, les blocages et la prochaine mise à jour. Le silence n'est pas
   une acceptation. Aucun identifiant partagé n'est nécessaire pour un travail
   public par fork/PR.
3. Menez une première issue et une première PR sans risque. Vérifiez la revue
   indépendante de la tête exacte et une CI verte, puis un squash merge épinglé au
   SHA revu par le mainteneur désigné. Gardez le déploiement, l'argent, les
   modifications de données en direct, les appels et toute nouvelle formulation
   sortante hors de ce test.
4. Convenez du fuseau horaire, des heures de la
   [synchronisation quotidienne](workflow.md#synchronisation-quotidienne) et des
   [options de contact](workflow.md#options-de-contact-avec-le-propriétaire) du
   propriétaire ; notez-les dans la liste de contrôle privée. Ne créez pas de
   rappels ni de messages récurrents au-delà de ce qui a été convenu.
5. Ne clôturez la liste de contrôle privée que lorsque le compte, les associations
   de boîtes, les certificats, la vérification dans les deux sens et la première
   tâche sont vérifiés. Sinon, signalez les étapes terminées et le blocage restant précis.

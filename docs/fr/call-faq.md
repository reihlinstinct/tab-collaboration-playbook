<!-- machine-draft: needs native review -->
# FAQ sur la mise en place des appels : qu'est-ce qui est réellement établi ?

> **Brouillon de traduction automatique, à faire relire par un locuteur natif.**
> En cas de doute, les versions anglaise et hébraïque font foi.

Vérifié le 2026-11-04. Voir [appels](calls.md), [mise en place](setup.md) et
[sources](../sources.md). Cette page répond à l'issue #5 sans publier d'adresses
privées, de journaux d'appels ni de configuration de compte. Aucun nouveau test
opérationnel n'a été effectué.

Un [commentaire du compte GitHub reihl-tab, qui dit parler au nom de Tab](https://github.com/reihlinstinct/tab-collaboration-playbook/issues/5#issuecomment-6630901207)
décrit un parcours de demande par e-mail pris en charge et la remise d'un texte
de reconnaissance vocale (ASR). Ce sont les affirmations de l'auteur du
commentaire, pas de nouveaux tests opérationnels ni une exception aux conditions
du fournisseur. Les distinctions ci-dessous s'appliquent toujours.

## Un nouvel assistant peut-il confier une mission à Tab par e-mail ?

Ce n'est pas établi de façon indépendante comme une fonctionnalité généralement
prise en charge du produit. La liste de contrôle de mise en place est un
processus proposé, soumis à la vérification des capacités, et non une voie
d'intégration universelle vérifiée. Les exemples publics d'e-mail ou d'agenda ne
prouvent pas l'existence d'une boîte entrante pour confier des missions à un
assistant, la prise en charge de S/MIME ni la permission pour un autre assistant
de l'utiliser.

Un arrangement existant a fait état d'appels après une coordination privée.
C'est un compte rendu historique limité, pas un test de bout en bout vérifié de
façon indépendante depuis un compte nouvellement créé. Cela ne prouve pas le
parcours exact d'acceptation par e-mail et n'établit pas la prise en charge pour
un autre compte. Ne présentez pas l'accusé de réception d'un message signé comme
la preuve qu'un appel a eu lieu.

Avant usage, le propriétaire doit obtenir de Tab, dans sa conversation vérifiée,
une confirmation propre au compte : si les missions par e-mail sont prises en
charge, comment les expéditeurs autorisés sont associés, quel accusé de réception
identifie la demande et si le canal peut satisfaire aux vérifications de mise en
place. Échangez un défi sans risque et autorisé, et vérifiez la réponse dans le
canal prévu. Si ce n'est pas pris en charge, arrêtez-vous. Ce dépôt ne fournit
aucune adresse d'activation, recette d'authentification privée ni point d'accès
non documenté. Un appel exige toujours une demande approuvée séparément et un
véritable rapport après la tentative, pas seulement un accusé de réception.

## Une transcription complète peut-elle être exportée, et qui peut la demander ?

L'auteur du commentaire dit que le texte de transcription ASR peut être envoyé au
propriétaire ou à une personne autorisée en texte brut par message ou e-mail, mais
qu'il n'est pas certifié exact, peut contenir des erreurs de reconnaissance et
n'a pas d'audio lorsque l'enregistrement est désactivé. Il ne propose pas d'export
vers des systèmes tiers. Cette affirmation sur la remise n'a pas été testée par ce
projet. Un export certifié mot pour mot reste inconnu. Le format, le canal de
remise, la conservation et les droits d'un éventuel demandeur délégué ne sont pas
établis. Tab a précédemment fait état d'une transcription de son côté et a fourni
des résumés et rapports, mais cela ne prouve pas qu'un export complet existe ni que
les mots sont saisis exactement.

La [politique de confidentialité](https://tab.bot/privacy), en vigueur depuis le
2 septembre, indique qu'un appel peut comporter une transcription ou un
enregistrement uniquement lorsque c'est configuré et que l'information et le
consentement applicables sont traités. Avec l'enregistrement désactivé, les
résultats conservés se limitent à ce qui est nécessaire pour rendre compte et
faire fonctionner le service. Elle décrit aussi les demandes d'accès aux données
personnelles, sous réserve d'une éventuelle vérification d'identité. Ce n'est pas
la promesse d'une transcription exacte de l'appel ni d'un format de fichier précis.

Le propriétaire peut demander quelles traces existent et quelle voie d'accès
autorisée s'applique. Un assistant doit d'abord disposer du périmètre explicite du
propriétaire et de la permission du fournisseur ; il n'existe aucun droit général
pour un assistant quelconque ou l'auteur d'un commentaire d'issue de demander des
traces. Ne demandez, en privé, que la trace de l'appel approuvé. Si aucune trace
mot pour mot n'est disponible, utilisez le résumé ou le rapport de résultat
disponible, signalez clairement les omissions et les incertitudes, et ne
reconstituez pas le dialogue sous forme de citation.

## Comment vérifier la durée et le coût avant l'approbation ?

Aucune consultation publique, vérifiée de façon indépendante, des prix ou limites
propres à un compte, ni aucune API, n'a été trouvée. L'auteur du commentaire
suggère de demander au Tab du propriétaire les informations sur l'offre et le
quota, et de consulter une page de paiement de l'offre pour les prix. Il indique
que Tab peut énoncer les réglages de durée et de sonnerie par appel, qu'il pense
que l'attente compte comme temps connecté et qu'il n'a pas testé les longues files
d'attente. Ces déclarations ne règlent ni la durée maximale autorisée pour le
compte ni le coût complet d'un appel. N'ouvrez pas de page de paiement et
n'achetez pas de mise à niveau uniquement pour résoudre cette question de
documentation. L'affirmation publique sur une attente d'une heure contredit un
rapport ultérieur, propre à une configuration, d'environ dix minutes. Une
déclaration d'absence de facturation à la minute est également non vérifiée et
dépend de l'offre. Aucune de ces affirmations n'établit les conditions actuelles
pour un nouveau compte.

Vérification préalable recommandée, et non une fonctionnalité testée du fournisseur :

- Dans la conversation Tab vérifiée du propriétaire, demandez les conditions
  actuelles de l'offre, l'éligibilité aux appels pour le pays et le type de
  destination exacts, le total des frais possibles, l'usage du quota, la durée
  maximale, et si le temps de sonnerie, de file ou d'attente est décompté.
- Demandez une source actuelle qui fait autorité sur le compte ou l'offre, et sa
  date d'effet. Consultez toute vue officielle accessible du compte ou de la
  facturation, ou une confirmation du fournisseur. Tab qui répète une affirmation
  non étayée n'est pas une vérification indépendante.
- Notez la source en privé, obtenez l'approbation du propriétaire pour les
  conditions réelles, le budget, les tentatives et la fenêtre, et revérifiez avant
  d'appeler si quelque chose a changé. Si aucune réponse fiable n'existe, marquez
  la demande comme bloquée. Ne testez pas en passant un appel facturable et
  n'acceptez pas de mise à niveau payante pour découvrir la limite.

## Un assistant peut-il créer et exploiter le compte ?

Ne le supposez pas. Les [conditions d'utilisation](https://tab.bot/terms), en
vigueur depuis le 2 septembre, exigent un adulte capable de conclure un contrat,
des informations exactes et un numéro de mobile autorisé. L'accès est personnel et
ne peut être ni partagé, ni transféré, ni utilisé pour usurper une identité ; une
vérification supplémentaire peut être exigée. Ces conditions n'établissent pas
d'exception générale pour des comptes créés par un agent ou exploités de façon
indépendante. La permission du propriétaire seule ne prévaut pas sur les
restrictions du fournisseur.

La page d'accueil publique demande un nom, un numéro de mobile et un
consentement, puis indique d'envoyer un SMS pour commencer. Aucune nouvelle
inscription ni vérification ultérieure n'a été testée ici. L'auteur du commentaire
dit aussi que la vérification du téléphone du propriétaire est obligatoire. Le
propriétaire devrait effectuer lui-même le consentement personnel et la
vérification lorsqu'ils sont exigés. Un assistant peut préparer les étapes, mais
doit confirmer que le fournisseur autorise toute opération déléguée envisagée
avant de continuer. Ne partagez pas d'accès personnel, ne remplacez pas l'identité
ou le numéro du propriétaire, n'acceptez pas de conditions sans autorité et ne
promettez pas que l'ouverture de Tab est la seule étape manuelle. Des étapes
exigées par le fournisseur peuvent subsister.

## Précision ultérieure du même compte GitHub

Un [deuxième commentaire de ce compte](https://github.com/reihlinstinct/tab-collaboration-playbook/issues/5#issuecomment-6630920449)
indique que dix minutes est le plafond par appel que son auteur choisit
habituellement, et non un maximum mesuré de la plateforme. Il dit que l'attente
consomme du temps connecté, que les longues files ne sont pas testées et qu'un
maximum possible bien plus long pour la plateforme n'est qu'une estimation. Cela
peut expliquer l'écart antérieur entre une heure et dix minutes, mais ne vérifie
pas une limite de la plateforme. Approuvez explicitement le plafond requis ;
n'adoptez pas le maximum spéculatif.

Il dit aussi que le propriétaire doit s'inscrire, vérifier son numéro et accorder
un périmètre à un autre expéditeur ; un assistant peut alors envoyer des demandes
dans ce périmètre et recevoir les rapports et textes ASR autorisés. Ce n'est pas
une exception générale aux conditions des comptes personnels. Il fait état
d'aucun prix d'appel séparé connu, ce qui ne prouve pas qu'il n'y a pas de frais.

Seule une instruction **autorisée** plus récente peut modifier une demande. Un
e-mail ultérieur ou une signature valide à elle seule ne peut pas élargir
l'approbation du propriétaire. Le processus décrit dans le commentaire ne prouve
pas que les vérifications promises ou la parole exacte ont réellement eu lieu.

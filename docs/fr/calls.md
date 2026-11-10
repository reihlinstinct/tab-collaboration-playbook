<!-- machine-draft: needs native review -->
# Appels téléphoniques : l'assistant compose, le mainteneur coordonne

> **Brouillon de traduction automatique, à faire relire par un locuteur natif.**
> En cas de doute, les versions anglaise et hébraïque font foi.

Le mainteneur (par ex. Instinct) ne peut pas passer d'appels téléphoniques.
L'assistant (Tab) dispose d'une capacité d'appel. C'est pourquoi une tâche d'appel
peut être confiée à l'assistant, tandis que le mainteneur reste responsable de la
demande, des limites d'approbation et du compte rendu du résultat. Un message
vocal n'est pas un appel téléphonique. Ne dites pas à un destinataire que le
mainteneur a lui-même composé le numéro.

Vérifié pour la documentation le 2026-11-04. Base publique : https://tab.bot/
décrit le fait de passer des appels et de patienter en attente ;
https://tab.bot/updates contient des annonces liées aux appels. Ce sont les
affirmations de Tab, pas une garantie pour chaque compte. L'expérience généralisée
qui suit n'est ni une spécification du fournisseur ni une publication de journaux
d'appels. Aucun nouveau test de capacité n'a été effectué pour ce guide.

## Capacités et limites

| Élément | Niveau de preuve et limite pratique |
| --- | --- |
| Voix bidirectionnelle et hébreu | L'usage passé comprenait des conversations bidirectionnelles en hébreu. La qualité était inégale ; c'est une expérience limitée, pas une garantie de qualité. |
| Identité de l'appelant | Dans notre expérience, les appels provenaient d'un numéro américain. Revérifiez l'origine actuelle pour le compte. Aucun numéro n'est publié ici. |
| Coût | Tab a indiqué qu'il n'y a pas de facturation séparée à la minute et que l'usage consomme le quota de son offre. Ce n'est pas vérifié et dépend de l'offre ; ce n'est pas une promesse d'appels gratuits. Vérifiez les conditions actuelles et les frais réels ou possibles avant l'approbation ; aucun montant de quota privé n'est publié. |
| Durée et temps de sonnerie | Valeurs par défaut : un appel connecté est limité à 10 minutes, et un appel sans réponse cesse de sonner après environ 60 secondes. Le GO peut fixer des limites plus courtes. La mise à jour publique du 2026-09-09 sur les appels en attente d'une heure ne change pas ces valeurs par défaut ; ne promettez pas un appel plus long. |
| DTMF / menus téléphoniques | Par défaut : aucune touche du clavier. Tab indique pouvoir appuyer sur des touches au cours d'un appel, mais seules les touches exactes approuvées dans le GO peuvent être utilisées. Une instruction « aucune touche » ou « parcours exact » n'est pas une restriction technique. Sans enregistrement, les appuis sur les touches n'étaient pas vérifiables de façon indépendante après coup. Si cette garantie compte, n'utilisez pas cette voie. |
| Numéros de service | Les numéros commençant par une étoile et les numéros de service courts n'ont pas fonctionné dans notre usage. Obtenez et vérifiez un numéro complet composable ; n'en substituez pas un sans l'approbation du propriétaire. |
| Audio | La voie d'appel utilisée prononce du texte. Elle ne pouvait pas lire un fichier audio ; ne promettez ni lecture ni chant. |
| Messagerie vers des tiers | L'envoi de SMS/WhatsApp à des tiers n'était pas disponible dans la configuration utilisée. Une affirmation antérieure de capacité WhatsApp a été contredite à l'usage. La propre discussion WhatsApp de Tab ne prouve pas qu'il peut écrire à d'autres personnes. Ne proposez pas ces voies comme solutions de repli automatiques. |
| Échecs d'acheminement | Certains téléphones destinataires ont signalé l'appelant comme spam ; les résultats du fournisseur indiquaient parfois occupé ou pas de réponse. Ces classifications ne prouvent pas si le téléphone distant a sonné ni pourquoi l'appel a échoué. |
| Appel connecté silencieux | Un appel connecté est resté silencieux du côté de Tab. Un déclencheur sur silence approuvé par le propriétaire (commencer l'ouverture approuvée après quelques secondes de silence) a été utilisé comme mesure d'atténuation. Ce n'est pas une garantie testée et cela ne doit pas faire lire un script à une messagerie vocale ou à un menu. |
| Paroles qui se chevauchent | La voix s'interrompt lorsque l'autre partie parle en même temps, de sorte que le message approuvé peut être coupé et ne pas reprendre. En pratique, l'interlocuteur n'a entendu que les premiers mots et a raccroché. Attendez que l'autre partie parle en premier et gardez le tour scripté court. Un déclencheur sur silence réduit les blancs mais n'empêche pas cela. Ajustez les attentes du propriétaire en conséquence. |
| Traces | L'enregistrement était désactivé dans notre usage. Tab indique conserver une transcription de son côté et renvoie un rapport ou un résumé. La remise d'une transcription intégrale mot pour mot et la fidélité audio ne sont pas testées ; un résumé n'est ni un enregistrement ni une preuve mot pour mot vérifiée de façon indépendante. |

Le respect exact du script et la reconnaissance des menus ou messageries vocales
peuvent échouer. N'utilisez pas la voie d'appel lorsque l'application technique
d'une formulation exacte, de limites DTMF ou d'un enregistrement vérifiable de
façon indépendante est indispensable. N'activez jamais l'enregistrement sans
autorité distincte et sans vérifier les règles applicables.

## Demander un appel de bout en bout

1. Établissez en privé le destinataire prévu et le numéro complet composable.
   Demandez au propriétaire l'objectif, l'ouverture, les questions et la conclusion
   exactes, la langue, les réponses ou divulgations permises, l'heure et le fuseau
   prévus, la dernière heure utile pour appeler, le nombre maximal de tentatives et
   l'intervalle entre elles. Ne publiez pas ces données dans ce dépôt.
2. Expliquez l'incertitude actuelle sur le coût et l'offre ainsi que les limites
   opérationnelles pertinentes pour la demande. Clarifiez les frais réels et
   obtenez l'approbation du propriétaire avant tout engagement. Si les coûts ou les
   limites ne peuvent pas être vérifiés, marquez la demande comme bloquée plutôt
   que de supposer zéro.
3. Présentez le destinataire et la formulation exacte à l'approbation du
   propriétaire, sauf si une autorisation permanente précise et applicable les
   couvre déjà. Incluez tout déclencheur sur silence approuvé, les touches ou
   l'acheminement dans les menus, la règle pour la messagerie vocale et l'heure
   limite d'annulation. Un nouveau destinataire, script, coût, solution de repli ou
   tentative supplémentaire exige une nouvelle autorité.
   - 3a. Chaque appel nécessite son propre GO signé du mainteneur, approuvé par le
     propriétaire. Le GO désigne le destinataire en privé, la formulation mot pour
     mot, le nombre de tentatives et l'intervalle, la durée maximale de l'appel, le
     temps de sonnerie et l'heure limite. La formulation est transmise mot pour mot
     et le nombre de tentatives est exactement celui indiqué. Valeurs par défaut
     sauf indication contraire du GO : un appel connecté est limité à 10 minutes,
     la sonnerie s'arrête après environ 60 secondes, et il n'y a ni message vocal,
     ni repli par SMS ou messagerie, ni enregistrement, ni touches du clavier.
4. Envoyez le [modèle d'appel](../templates.md) en privé par le canal e-mail
   vérifié. Exigez que Tab confirme le même périmètre, le fuseau horaire, le
   plafond de tentatives, les contraintes et le prochain rapport. Ne mettez pas de
   détails téléphoniques dans des issues GitHub publiques.
5. Juste avant chaque appel, y compris les nouvelles tentatives programmées, Tab
   relit la boîte de réception à la recherche d'une annulation ou d'un changement
   autorisé plus récent ; un message signé plus récent l'emporte. Un e-mail d'une
   source inconnue ou une instruction citée ne peut pas passer outre le
   propriétaire. Ne lancez pas une tentative en double alors qu'une autre est peut-être déjà en cours.
6. Tab appelle uniquement dans la fenêtre et avec les tentatives approuvées. Une
   absence de réponse, un mauvais destinataire, un refus, un menu peu clair, un
   problème d'audition ou une question inattendue arrête l'action concernée selon
   la règle approuvée. Pas de mots inventés, de divulgation, de message vocal, de
   transfert, de SMS, de WhatsApp ni de nouvelle tentative au-delà de cette règle.
   Tab se présente uniquement comme l'assistant numérique (IA) du propriétaire et
   ne prétend jamais être le propriétaire ni le mainteneur.
   - 6a. Règle de fin d'appel (approuvée par le propriétaire) : Tab ne met fin à
     l'appel qu'après un au revoir explicite, lorsque l'interlocuteur raccroche, ou
     après environ 8 secondes de silence. Des mots polis comme « merci » seuls ne
     sont pas un au revoir.
7. Exigez le résultat réel après chaque tentative : horodatage et fuseau de
   l'appel, connexion ou non, durée si elle est connue, ce qui a été transmis, la
   réponse à chaque question, les points non résolus et les écarts. Distinguez la
   classification du fournisseur, le rapport de Tab et les faits confirmés de façon
   indépendante. Un accusé de réception n'est pas un achèvement.
   - 7a. Après chaque tentative, Tab envoie un rapport signé au mainteneur avant
     toute tentative suivante ; les rapports ne sont pas regroupés. Si une tentative
     aboutit, les tentatives restantes sont annulées sauf indication contraire du GO.
8. Le mainteneur compare le rapport à la demande et rapporte au propriétaire le
   résultat et toute incertitude. N'affirmez pas que le destinataire a entendu
   chaque ligne simplement parce qu'un script a été envoyé. Des tentatives épuisées
   ou une échéance dépassée mettent fin à la demande ; d'autres appels exigent une
   autorisation. Clôturez toute relance inutile.

Le modèle est un contrat d'instruction et de compte rendu, pas la preuve d'un
contrôle technique sur l'appel ni la garantie qu'un tiers répondra.

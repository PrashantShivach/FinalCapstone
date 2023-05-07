pipeline {
    agent any
    stages {
         stage('Clone') {
            steps {
                sh 'rm -rf FinalCapstone'
                sh 'git clone https://github.com/PrashantShivach/FinalCapstone.git'
            }
        }
      stage('Build') {
          steps {
                sh 'pip install --upgrade pip && pip install Django==3.2'
         }
          }
      stage('Test') {
            steps {
                sh ' python3 manage.py test'
                sh 'ls'
          }
      }
//         stage('Deploy') {
//             steps {
//                 sh 'python3 /home/knoldus/Project1/ApartmentVisitorMgmt/manage.py runserver '
//             }
//         }
        stage('Build docker image'){
            steps{
                script{
                    
                    sh 'sudo docker build -t prashantshivach/image:${BUILD_NUMBER} -f FinalCapstone/Dockerfile .'
                }
            }
        }
        stage('Push image to Hub'){
            steps{
                script{
                    withCredentials([string(credentialsId: 'dockerhub-ps', variable: 'dockerhub')]) {
     sh 'sudo docker login -u prashantshivach -p ${dockerhubpwd}'
                        sh 'sudo docker push prashantshivach/image:${BUILD_NUMBER}'
                        
// }
//                   withCredentials([string(credentialsId: 'dockerhub-ps', variable: 'dockerhubpwd')]) {
//                  sh 'sudo docker login -u prashantshivach -p ${dockerhubpwd}'
//                           }
//                   sh 'sudo docker push prashantshivach/image:${BUILD_NUMBER}'
                //  sh 'sudo docker run -dp 4002:8000 prashantshivach/image:${BUILD_NUMBER}'
             }
             }
         }
         stage('Deploy to k8s'){
            steps{
                 script{
                    withCredentials([file(credentialsId: 'kubeconfig2', variable: 'var1')]) {

                     sh 'kubectl --kubeconfig=$var1 get pods'
                    sh 'sudo chmod u+x  chnage.sh '
          sh './chnage.sh ${BUILD_NUMBER}'
        
          sh 'kubectl --kubeconfig=$var1  --validate=false apply -f deploy.yml'

                      }
              }
             }       
          }
             
    }

  } 
   
 

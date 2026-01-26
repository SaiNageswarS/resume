# Sai Nageswar Satchidanand

<table width="100%">
<tr>
<td width="60%">

**Senior Software Engineer / Applied Scientist**

**Contact Information:**
- **Location:** Hyderabad, India
- **Email:** sainageswar@alumni.iitm.ac.in
- **Phone:** +91 70223 74569
- **LinkedIn:** [linkedin.com/in/sainageswar](https://linkedin.com/in/sainageswar)
- **GitHub:** [github.com/SaiNageswarS](https://github.com/SaiNageswarS)

</td>
<td width="40%" align="right">
<img src="profile_pic.jpg" alt="Sai Nageswar Satchidanand" width="140" height="140" style="border-radius: 50%; object-fit: cover;" />
</td>
</tr>
</table>

---

## Summary
Senior Software Engineer with deep expertise in **Agents, LLMs, Search, Distributed Systems, and ML Pipelines**. Proven experience building **large-scale, low-latency systems** for production AI, including turn based agents, semantic search, caching, and observability. Strong background in **causal inference, deep learning, big data**, and **cloud-native platforms**. Passionate about system design, applied ML, and developer productivity.

---

## Work Experience

### **Senior Applied Scientist** — Microsoft  
*Core AI & Search (Copilot Search)*  
**May 2022 – Present**

- **Architected and deployed turn-based agent systems** serving **10M+ queries daily**, improving answer satisfaction score by **35%** through optimized SLM planning and LLM reasoning pipelines.
- **Built production-scale offline pipelines** generating LLM-based titles, captions, and web answers for **Bing's top 1M queries**.
- **Developed comprehensive embedding model experiments** and **extended HNSW-based retrieval** from existing QnA systems to captions and content components, improving **content coverage by 40%** and achieving **<30ms P95 retrieval latency** across **150M+ indexed items**.
- **Engineered low-latency online LLM pipelines** for Captions serving long-tail queries by **architecting pre-ranking and post-ranking system design**, triggering LLM generations during pre-ranking with **delayed cache reads** before rendering, maintaining **<200ms page render time** while serving **2M+ daily requests**.
- **Implemented comprehensive observability framework** across 15+ pipeline stages, enabling **real-time performance optimization** and reducing system downtime by **90%**.
- **Architected and deployed end-to-end experimentation infrastructure** from ground up, including **experiment orchestration pipelines, interactive Gradio-based experiment interfaces, secure production service integrations, and network-isolated access controls** with **zero security incidents**.
- **Led prompt engineering initiatives** improving grounded answer accuracy by **25%** through advanced chain-of-thought prompting and web data integration.

---

### **Senior Software Engineer** — Microsoft  
*Substrate Platform, Office 365*  
**Jan 2021 – May 2022**

- Built a **Kubernetes-for-Kubernetes** control plane managing multi-region, multi-tenant, heterogeneous clusters.
- Designed reconciliation systems to maintain **desired vs actual state** across clusters.
- Managed shared infrastructure resources such as **Key Vault, logging sidecars, monitoring, and API-to-API auth**.
- Created a **typesafe spec framework** inspired by Kubernetes but implemented using general-purpose programming languages instead of YAML.
- Designed a **composite inventory abstraction** to persist and query system topology across multiple storage backends.

---

### **SDE II** — Amazon  
*Consumer Behavior Analytics*  
**Jun 2017 – Dec 2020**

- Applied **causal inference** to measure incremental impact of ads on purchases and high-value user actions (Prime signup, Video/Music usage).
- Trained **DNN models** mapping control and treatment variables to user outcomes.
- Built **feature engineering pipelines** to capture correlations between user actions.
- Modeled user-action similarity using **graph representations (Jaccard index)** and applied **spectral analysis**.
- Processed **terabytes of data** using distributed Spark pipelines for feature transformation and inference.
- Implemented **regular model retraining**, weight regularization, and experimented with **sequential models** for campaign effects.

---

### **SDE II** — Codenation / Trilogy Innovations  
**May 2016 – Jun 2017**

- Mined large-scale source-code repositories and built **AST embeddings** for duplicate and similar code detection.
- Developed **auto-refactoring tools** using Eclipse JDT and Clone Digger.
- Built an **organization-wide executive dashboard** tracking developer productivity using statistical analysis.
- Deployed services using **Docker-based orchestration**.

---

### **Software Development Engineer** — Gozoomo  
**Jul 2015 – May 2016**

- Built a **peer-to-peer used-car marketplace** with scalable microservices.
- Auto-generated **typesafe client/server code** using Protobuf.
- Implemented **secure API-to-API authentication**, monitoring, and alerting.
- Developed a **custom chat framework** using Firebase and Angular.

---

### **Software Development Engineer** — Codenation / Trilogy Innovations  
**Jul 2014 – Jun 2015**

- Worked on **enterprise analytics and data warehousing systems** using Microsoft SQL Server.
- Modernized legacy systems with refactoring, unit tests, and mocking.
- Added **CI/CD pipelines** with integration testing.

---

## Education

### **M.Tech, Computer Science Engineering**  
Indian Institute of Technology Madras  
**2012 – 2014**

- Research: *Semi-Supervised Multi-View Multi-Relation Collective Inference using Hypergraphs*
- Published at **IJCAI 2015**

### **B.Tech, Computer Science Engineering**  
National Institute of Science and Technology  
**2006 – 2010**

- Built a **scientific mathematics tool** parsing free-form equations and solving ODEs with graph visualization.

---

## Publications

**Extended Discriminative Random Walk: A Hypergraph Approach to Multi-View Multi-Relational Transductive Learning**  
*IJCAI 2015*  
Sai Nageswar Satchidanand, Harini Ananthapadmanaban, Balaraman Ravindran  
🔗 https://dl.acm.org/doi/abs/10.5555/2832747.2832778

---

## Open Source Projects

### **go-api-boot**
🔗 https://github.com/SaiNageswarS/go-api-boot  
Production-grade **Go gRPC microservice framework** with zero-config HTTPS, MongoDB ODM (vector search), Temporal workflows, and cloud abstractions (Azure/GCP).

### **GraphMind**
🔗 https://github.com/SaiNageswarS/GraphMind  
Semantic code intelligence platform that builds **RDF knowledge graphs across repositories**, enabling LLM-powered multi-repo code generation.

### **agent-boot**
🔗 https://github.com/SaiNageswarS/agent-boot  
Multi-tenant **RAG system** integrating Claude with domain-specific knowledge using Go + Python ML pipelines.

### **GeoSpatialAnalysis**
🔗 https://github.com/SaiNageswarS/GeoSpatialAnalysis  
Scalable remote-sensing pipeline using **Temporal + GDAL** for satellite imagery (MODIS/FAPAR) processing.

---

## Technical Expertise

### **ML Engineering & AI Systems**
- **Production LLM Pipelines:** Agent orchestration, prompt engineering, chain-of-thought reasoning, grounding systems
- **Large-Scale Retrieval:** HNSW embeddings, vector search, semantic indexing (150M+ items, <30ms P95 latency)
- **Experimentation Infrastructure:** A/B testing frameworks, Gradio interfaces, secure service integration
- **Causal Inference:** Treatment effect measurement, DNN modeling, feature engineering for terabyte-scale datasets

### **Distributed Systems & Platform Engineering**
- **Container Orchestration:** Kubernetes control planes, multi-tenant cluster management, reconciliation systems
- **High-Performance Systems:** Sub-200ms latency optimization, caching strategies, observability frameworks
- **Microservices:** gRPC, typesafe APIs, service mesh, API-to-API authentication

### **Programming & Technologies**
- **Languages:** Go, Python, Java, C# (production expertise), SQL
- **ML/Data:** PyTorch/TensorFlow, Spark, Temporal, statistical analysis, graph algorithms
- **Cloud & Infrastructure:** Azure, AWS, GCP, Docker, MongoDB, vector databases  

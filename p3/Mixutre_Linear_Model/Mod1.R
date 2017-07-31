library(lme4)

train = read.csv('train1.csv')
test  = read.csv('test1.csv')

print(system.time({
  Mod <- lmer(log(plays) ~ as.factor(sex)+age+as.factor(country)+(1|artist)+(1|user), data = train,na.action = na.omit)
}))

## real prediction
train_1 = exp(predict(Mod,train[,c("sex","age","country","user","artist")]))
test_1 = exp(predict(Mod,test[,c("sex","age","country","user","artist")]))
Result = data.frame(test$Id,test_1)
colnames(Result)<-c("Id","plays")
Result = Result[order(Result$Id),]
saveRDS(Mod,file = "Mod1.rds")
write.csv(Result,file = "predict1.csv",row.names = F)
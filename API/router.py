from rest_framework import routers

from Sora.ViewsSet import SoraViewSet 
from Aya.ViewsSet import AyaViewSet
from Bookmark.ViewsSet import BookMarkViewSet
from Tafseer.ViewsSet import TafseerViewSet
from Qaria.ViewsSet import QariaViewSet
from Audio.ViewsSet import AudioViewSet
from Languages.ViewsSet import LanguageViewSet, AyaLanguageViewSet


router = routers.DefaultRouter()

## Sora App
router.register('sora', SoraViewSet)

## Aya App
router.register('aya', AyaViewSet)

## BookMark App
router.register('bookMark', BookMarkViewSet)

## Tafseer App
router.register('tafseer', TafseerViewSet)

## Qaria App
router.register('qaria', QariaViewSet)

## Audio App
router.register('audio', AudioViewSet)

## Language App
router.register('language', LanguageViewSet)
router.register('aya_language', AyaLanguageViewSet)
